# 🚨 RegTech Change Monitor

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Automated Checks](https://img.shields.io/badge/automation-GitHub%20Actions-lightgrey.svg)](https://github.com/features/actions)
[![Status](https://img.shields.io/badge/status-PoC-orange.svg)]()

---


🧩 The Problem

Most Governance, Risk & Compliance (GRC) teams still track regulatory updates manually.
Every week, analysts visit dozens of websites — like the EU AI Act, NIS2 Directive, or ISO/IEC 27001 pages — to check for changes.

This process is time-consuming, inconsistent, and offers no audit trail.
Missed updates can lead to compliance gaps, audit findings, or regulatory penalties.

💡 My Solution

I built the RegTech Change Monitor, a Python-based Proof of Concept (PoC) that automates regulatory monitoring. 

The system automatically checks official regulation pages daily, compares new content with approved baselines, and logs every change — all version-controlled in Git for auditable traceability.


### 🏗️ What I Built

| Component | Purpose |
|------------|----------|
| `monitor.py` | Core engine that fetches pages, extracts content via CSS selectors, compares with baselines, and logs changes. |
| `config/monitor_targets.json` | Defines which regulatory pages and sections to track. |
| `status_log.json` | Maintains change history and audit trail. |
| GitHub Actions Workflow | Automates daily monitoring runs and commits results. |

---

### 🧰 Tech Stack
- **Language:** Python 3.9+  
- **Libraries:** `requests`, `beautifulsoup4`, `python-dotenv`, `json`  
- **Automation:** GitHub Actions / Windows Task Scheduler  
- **Data & Logging:** JSON + Git commits as immutable audit evidence  

---

🧠 How It Works

🧩 Input: JSON list of regulatory websites and CSS selectors

⚙️ Engine: Python script (monitor.py) scrapes pages, detects changes, and updates logs

🔐 Storage: Approved baselines and status_log.json files maintained in Git

🤖 Automation: GitHub Actions executes daily checks, commits results, and alerts analysts when content changes

👩‍💼 Analyst Review: Analysts validate detected changes, perform risk assessments, and approve baselines


### 📤 Output

| Artifact | Description |
|-----------|--------------|
| `config/*_baseline.txt` | Stores the last approved version of each monitored regulation. |
| `config/status_log.json` | Machine-readable audit log containing run timestamps and status entries. |

| **Git Commit History** | Immutable audit trail showing every monitoring event and change. |

#### 🧾 Example Output Log
[2025-10-18 08:00:03] INFO - Checking target: NIS2 Directive
[2025-10-18 08:00:05] INFO - Status: OK (No change)
[2025-10-18 08:00:06] 🚨 ALERT - CHANGE DETECTED in EU AI Act content!



---

### 🌱 Future Enhancements

| Feature | Description |
|----------|--------------|
| 🔔 **Notifications** | Integrate Slack, Teams, or Email alerts for detected changes. |
| 🧠 **AI Drift Detection** | Use NLP models to detect semantic (meaning-level) policy changes. |
| 🪞 **Visual Diff Viewer** | Generate side-by-side text comparisons for analyst review. |
| 📦 **GRC Platform Integration** | Sync with tools like ServiceNow, Archer, or Jira for automated control updates. |
| 🗄️ **Database Persistence** | Add SQL or MongoDB backend for long-term storage and analytics. |
