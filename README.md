# 🛡️ NetProbe-Secure: Automated Attack Surface Management (ASM)

## 📌 Overview

NetProbe-Secure is a lightweight, automated Attack Surface Management (ASM) pipeline built with Python. It continuously monitors target infrastructure by scheduling Nmap scans, storing the results as a baseline, and comparing new scans against historical data.

Designed with SOC (Security Operations Center) workflows in mind, it detects infrastructure drift, scores the risk of newly exposed services, and generates automated HTML reports to alert security teams of potential vulnerabilities.

## ✨ Key Features

- **Automated Reconnaissance:** Executes scheduled Nmap scans based on customizable YAML profiles.
- **Stateful Baseline Tracking:** Stores historical scan data securely in a local SQLite database (`baseline.db`).
- **Intelligent Diff Engine:** Compares current scan results against the baseline to detect added/removed ports and version changes.
- **Risk Scoring:** Automatically assigns severity levels (HIGH, MEDIUM, LOW) based on the type of exposure detected.
- **Automated Reporting:** Generates a color-coded, easy-to-read HTML dashboard summarizing the attack surface state.
- **Set-and-Forget Automation:** Includes a Windows Batch orchestrator (`run_asm.bat`) designed to plug directly into Windows Task Scheduler for continuous monitoring.

## 🏗️ Architecture & Execution Flow

1. **Input Layer:** Reads targets from `config/targets.yaml` and scan arguments from `config/scan_profile.yaml`.
2. **Scanning Layer:** `nmap_runner.py` executes the scan and saves an XML output.
3. **Parsing Layer:** `nmap_parser.py` extracts relevant data (IP, Port, Protocol, Service, Version).
4. **Baseline Layer:** `baseline_manager.py` fetches the previous state from SQLite.
5. **Analysis Layer:** `diff_engine.py` identifies delta changes, and `risk_scoring.py` evaluates the severity.
6. **Output Layer:** `alert_engine.py` and `report_generator.py` notify the user and build the HTML report.

## 🚀 Prerequisites

Before running the tool, ensure you have the following installed:

- **Python 3.x**
- **Nmap:** Installed and accessible. _(Note: Ensure the path in `nmap_runner.py` matches your Nmap installation directory, e.g., `C:\Program Files (x86)\Nmap\nmap.exe`)_

## 🛠️ Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/CodebyDeshma-27/Attack-Surface-Management

   ```
2. **Configure your targets**
Edit config/targets.yaml to include the IPs or domains you have permission to scan:
targets:
  - 127.0.0.1
  - 192.168.1.50