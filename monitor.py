import requests
from bs4 import BeautifulSoup
import os # <--- FIXED: os module imported first
import json
from datetime import datetime
from dotenv import load_dotenv

print("--- SCRIPT STARTED SUCCESSFULLY ---") # <--- ADD THIS LINE

# Load environment variables from .env file
load_dotenv()

# --- Global Configuration & File Paths ---
TARGETS_FILE = "config/monitor_targets.json" # New file for multiple URLs
STATUS_LOG_FILE = "config/status_log.json"

# --- Logging Function ---

def log_status(status_type, regulation_name, message, url):
    """Writes a structured status update to a JSON log file (Audit Trail)."""
    
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # 1. Load existing logs
    logs = []
    if os.path.exists(STATUS_LOG_FILE):
        with open(STATUS_LOG_FILE, 'r') as f:
            try:
                logs = json.load(f)
            except json.JSONDecodeError:
                print(f"[WARNING] Status log file '{STATUS_LOG_FILE}' is corrupt or empty. Starting new log.")
                logs = [] 

    # 2. Create the new log entry
    new_entry = {
        "timestamp": timestamp,
        "status": status_type,
        "regulation": regulation_name,
        "message": message,
        "url": url
    }
    
    logs.append(new_entry)
    
    # 3. Save the updated logs
    os.makedirs(os.path.dirname(STATUS_LOG_FILE), exist_ok=True)
    with open(STATUS_LOG_FILE, 'w') as f:
        json.dump(logs, f, indent=4)
    
    print(f"[{status_type}] {regulation_name}: Logged update.")


# --- Core Logic Functions ---

def get_target_content(url, selector_id, regulation_name):
    """Fetches the webpage and extracts content using a specific HTML selector."""
    
    if not url or not url.startswith(('http://', 'https://')):
        log_status("ERROR", regulation_name, "Invalid or missing TARGET_URL in configuration.", "N/A")
        return None

    if not selector_id:
        log_status("ERROR", regulation_name, "Missing SELECTOR_ID in configuration. Cannot parse content.", url)
        return None

    try:
        headers = {'User-Agent': 'RegTech-Monitor-Bot/1.0'}
        response = requests.get(url, headers=headers, timeout=15)
        response.raise_for_status() 

        soup = BeautifulSoup(response.content, 'html.parser')

        content_element = soup.select_one(selector_id)
        
        if content_element:
            return content_element.get_text(separator=' ', strip=True)
        else:
            error_msg = f"HTML selector '{selector_id}' not found on page. Check the DevTools output."
            log_status("ERROR", regulation_name, error_msg, url)
            return None

    except requests.exceptions.RequestException as e:
        error_msg = f"Failed to fetch URL. Connection/HTTP error: {e}"
        log_status("ERROR", regulation_name, error_msg, url)
        return None


def monitor_single_target(target):
    """Monitors one regulation based on the provided configuration dictionary."""
    
    regulation_name = target["regulation_name"]
    target_url = target["target_url"]
    selector_id = target["selector_id"]
    
    # Create unique file names based on the regulation name (for auditability)
    safe_name = regulation_name.replace(" ", "_").replace("-", "_").lower()
    target_baseline_file = f"config/{safe_name}_baseline.txt"
    target_new_content_file = f"config/{safe_name}_new_content.txt"
    
    current_content = get_target_content(target_url, selector_id, regulation_name)

    if not current_content:
        # Error already logged in get_target_content, simply exit this routine
        return
    
    # 1. Load Baseline
    baseline_content = ""
    baseline_exists = os.path.exists(target_baseline_file)
    
    if baseline_exists:
        with open(target_baseline_file, 'r', encoding='utf-8') as f:
            baseline_content = f.read()
    
    # 2. Compare Content
    if current_content != baseline_content:
        
        if not baseline_exists:
            message = "Initial baseline set on first successful run. Monitor is active."
            log_status("INITIAL_BASELINE", regulation_name, message, target_url)
        else:
            message = f"Content has changed. New content saved to {target_new_content_file} for manual GRC review."
            log_status("CHANGE_DETECTED", regulation_name, message, target_url)
            
            # --- ACTION: Save new content for manual review ---
            os.makedirs(os.path.dirname(target_new_content_file), exist_ok=True)
            with open(target_new_content_file, 'w', encoding='utf-8') as f:
                f.write(current_content)
            
            # Print the critical alert to the console/log
            print(f"""
🚨 CHANGE DETECTED: {regulation_name}! 🚨
New content saved to: {target_new_content_file}

**MANUAL GRC ACTION REQUIRED:** 1. Review the changes in {target_new_content_file}.
2. If approved, manually copy {target_new_content_file} to {target_baseline_file} 
   and commit the change to Git.
""")

        # --- ACTION: Overwrite Baseline (Prevents logging spam on next run) ---
        os.makedirs(os.path.dirname(target_baseline_file), exist_ok=True)
        with open(target_baseline_file, 'w', encoding='utf-8') as f:
            f.write(current_content)

    else:
        log_status("OK", regulation_name, "Content matches baseline.", target_url)
        
    print("-" * 30) # Separator for multiple regulation checks


def load_targets():
    """Loads all monitoring targets from the JSON configuration file."""
    try:
        with open(TARGETS_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"CRITICAL ERROR: Monitoring target file not found: {TARGETS_FILE}. Create it based on the example.")
        return []
    except json.JSONDecodeError as e:
        print(f"CRITICAL ERROR: Invalid JSON format in {TARGETS_FILE}. Check for syntax errors. Error: {e}")
        return []


def run_monitor():
    """Reads all targets and runs the monitoring routine for each one."""
    
    targets = load_targets()
    
    if not targets:
        return
        
    print(f"\n--- Starting RegTech Monitor: Checking {len(targets)} Regulations ---")

    for target in targets:
        monitor_single_target(target)
        
    print("--- Monitoring Complete ---")

if __name__ == "__main__":
    run_monitor()