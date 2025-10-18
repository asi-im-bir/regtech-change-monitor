# 🚨 RegTech Change Monitor (Multi-Target PoC)

## 🎯 Project Status and Value Proposition

This is a **Proof of Concept (PoC)** demonstrating automated, audit-ready Governance, Risk, and Compliance (GRC) monitoring. We transition critical regulatory oversight (e.g., **NIS2, AI Act, ISO 27001**) from a manual process to a reliable, version-controlled system.

The tool directly supports **Continuous Risk Assessment** and **Control Gap Analysis** by:

  * **Automating Intelligence:** Eliminates manual, daily checking of multiple regulatory body websites.
  * **Creating an Audit Trail:** Logs every check and change to version-controlled files on Git.
  * **Enforcing Change Control:** Triggers a clear alert when a policy baseline shifts, requiring mandatory human GRC approval.

-----

## 💻 Technical Architecture Overview

The system operates using a **Human-in-the-Loop** model. The automation handles detection (low value, high frequency), and the GRC analyst handles risk assessment (high value, low frequency).

| Component | File/System | Function / Outcome |
| :--- | :--- | :--- |
| **Input Scope** | `config/monitor_targets.json` | **Defines the Scope:** Central list of all monitored URLs and their unique CSS selectors. |
| **The Engine** | `monitor.py` | **Executes:** Runs the check loop, fetching data and performing string comparison. |
| **Audit Artifacts** | `config/*_baseline.txt` & `status_log.json` | **Stores Truth:** Holds the last approved policy text and the history of successful checks. |
| **Automation** | GitHub Actions / Task Scheduler | **Schedules:** Guarantees daily execution of the script (`cron`). |

-----

## 🛠️ Getting Started (Deployment Guide)

### Requirements

  * Python 3.8+
  * The required libraries: `requests`, `beautifulsoup4`, `python-dotenv`, and `json` (installed via `requirements.txt`).

### Setup Steps

1.  **Clone the Repository:**

    ```bash
    git clone [Your Repository URL]
    cd regtech-change-monitor
    ```

2.  **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3.  **Configure Targets (`config/monitor_targets.json`):**

      * Open this JSON file and define the full list of regulations you need to monitor.
      * **CRITICAL:** Ensure the `selector_id` is verified using F12 DevTools for each `target_url`.

4.  **Configure Environment (`.env`):**

      * Create a local copy: `cp config/.env.example .env`
      * Set the top-level `REGULATION_NAME` for general log identification (e.g., `"Company GRC Regulatory Watch"`).

-----

## 🚀 Usage, Validation, and GRC Workflow

### 1\. Initial Run (Baseline Establishment)

The first run connects to all sites and creates the initial reference files.

```bash
python monitor.py
```

**Verification:** Check the `config/` folder. It should contain **multiple unique `*_baseline.txt` files** and **`status_log.json`** with entries marked `"status": "INITIAL_BASELINE"`.

### 2\. Automated Run and Change Control

This is the fully automated GRC workflow after initial setup.

| Event | Action by Automation | GRC Analyst Action Required |
| :--- | :--- | :--- |
| **Daily Check** | Script runs, logs **`status: OK`** for stable targets, and automatically commits `status_log.json` to Git. | **No action.** System is confirmed stable. |
| **Alert/Change** | Script prints the **🚨 CHANGE DETECTED** alert and creates **`*_new_content.txt`**. | **IMMEDIATE REVIEW:** Analyst compares `*_new_content.txt` against the old baseline in Git history, performs **Risk Assessment**, and then **manually commits** the new baseline text to approve the change. |

### 3\. Production Scheduling (Automation)

The system must run daily.

| System | Command/Setup | Notes |
| :--- | :--- | :--- |
| **GitHub Actions** | Set up the `regtech_monitor.yml` workflow to run on a `cron: '0 8 * * *'` schedule. | **Preferred Method:** Ensures auditable, remote execution. |
| **Windows Task Scheduler** | Set up a Daily Task to run the Python executable with the full script path as an argument. | Suitable for local machine execution. |
