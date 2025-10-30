# 🚨 RegTech Change Monitor (Multi-Target PoC)

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Automated Checks](https://img.shields.io/badge/automation-GitHub%20Actions-lightgrey.svg)](https://github.com/features/actions)
[![Status](https://img.shields.io/badge/status-PoC-orange.svg)]()

---

⚡ RegTech Change Monitor — Automating Compliance for a Smarter GRC Future
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


### ⚙️ Inputs & Outputs

**Input:**  
`config/monitor_targets.json`  
```json
[
  {
    "name": "NIS2 Directive",
    "target_url": "https://digital-strategy.ec.europa.eu/en/policies/nis-directive",
    "selector_id": "#main-content"
  },
  {
    "name": "EU AI Act",
    "target_url": "https://artificialintelligenceact.eu/",
    "selector_id": ".article-body"
  }
]
Output:

config/*_baseline.txt — Last approved version of each monitored policy.

config/status_log.json — Structured audit log of all checks and detections.

Git history — Immutable evidence trail of every run and change.


🗂️ *_baseline.txt → Approved regulation content snapshot

📘 status_log.json → Machine-readable audit log

🕓 Git commits → Immutable evidence of checks and changes

Example:

[2025-10-18 08:00:06] 🚨 ALERT - CHANGE DETECTED in EU AI Act content!


🌱 Future Enhancements

🔔 Email / Slack notifications for detected changes

🧠 AI-based semantic drift detection (understanding legal meaning shifts)

📦 Integration with GRC platforms (ServiceNow, Archer, etc.)

🪞 Visual diff comparison of updated text
