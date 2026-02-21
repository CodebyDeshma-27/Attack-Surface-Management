from scanner.nmap_runner import run_nmap
from scanner.nmap_parser import parse_nmap_xml
from baseline.baseline_manager import init_db, save_baseline, load_baseline
from diff.diff_engine import diff_scans
from diff.risk_scoring import score_risk
from alerts.alert_engine import generate_alerts
from alerts.report_generator import generate_html_report

def main():
    init_db()
    run_nmap()

    new_scan = parse_nmap_xml()
    old_scan = load_baseline()

    diff = diff_scans(old_scan, new_scan)
    risks = score_risk(diff)

    alerts = generate_alerts(risks)
    generate_html_report(risks)

    save_baseline(new_scan)

    if alerts:
        print("⚠️ HIGH RISK CHANGES DETECTED")
    else:
        print("✅ No critical changes")

if __name__ == "__main__":
    main()
