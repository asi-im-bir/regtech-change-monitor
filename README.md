# 🚨 RegTech Change Monitor (Python PoC)

### **Project Status**

**POC (Proof of Concept)**. Built in under one hour to demonstrate automated governance, risk, and compliance (GRC) monitoring for critical regulations like NIS2, AI Act, and ISO standards.

---

### 💡 Project Value & Context

This tool directly addresses the challenge of managing a **Control Framework Transition** (like migrating VICS IT to ISO 27001) in a dynamic regulatory environment.

As a Control Framework Specialist, this script:
1.  **Automates Intelligence Gathering:** Replaces manual checking of regulatory body websites.
2.  **Ensures Timely Compliance:** Triggers immediate alerts for changes in compliance deadlines (e.g., NIS2 transposition).
3.  **Feeds the ISMS:** Provides the crucial input required for continuous **Risk Assessment** and **Control Gap Analysis**.

### 🛠️ Getting Started

This monitor is built in Python and uses a simple baseline file for change detection.

#### **Requirements**

* Python 3.8+
* A dedicated email account or **App Password** configured to send SMTP emails.

#### **Setup Guide**

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/your-username/regtech-change-monitor.git](https://github.com/your-username/regtech-change-monitor.git)
    cd regtech-change-monitor
    ```

2.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Configure Environment Variables:**
    * Copy the example file to create your local secret file:
        ```bash
        cp config/.env.example .env
        ```
    * **Edit the new `.env` file** and replace all placeholder values (especially `SMTP_PASSWORD`, `TARGET_URL`, and `SELECTOR_ID`) with your actual, private values.

4.  **Find the HTML Selector (Crucial Step!):**
    * Open your target regulatory URL (e.g., the EU AI Act page) in a browser.
    * Press **F12** to open Developer Tools.
    * Use the element picker (usually a small arrow icon) to click on the main text block you want to monitor.
    * Find the unique **ID** or **Class** name associated with that element (e.g., `id="content-main"`) and set the `SELECTOR_ID` value in your `.env` file accordingly.

### 🚀 Usage and Deployment

#### **1. Initial Run**

Run the script once to establish the initial baseline. It will save the content to `config/baseline.txt` and send an "INITIAL BASELINE SET" email (unless manually modified).

```bash
python monitor.py
### 🚀 Usage and Deployment

#### **2. Production Scheduling (Automation)**

To ensure continuous monitoring, schedule the script to run daily (e.g., every morning at 8:00 AM) using your system's native scheduler.

| System | Command/Setup | Notes |
| :--- | :--- | :--- |
| **Linux/macOS (Cron)** | `0 8 * * * /usr/bin/python3 /path/to/monitor.py` | Ensure you use the full path to your Python executable and the script. |
| **Windows (Task Scheduler)** | Set up a Daily Task to run the **Program/script** (`C:\...\Python310\python.exe`) with the **Argument** being the full path to `monitor.py`. | **CRITICAL:** Configure the task to run the Python executable, not the script file directly, and use the 'Start in' directory. |

For a detailed, step-by-step graphical guide on configuring the Windows Task Scheduler, please see the project **Wiki/Deployment Runbook.**