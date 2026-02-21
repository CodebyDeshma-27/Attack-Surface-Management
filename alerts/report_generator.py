def generate_html_report(risks, path="output/report.html"):
    html = "<h1>Attack Surface Report</h1><ul>"

    for r in risks:
        html += f"<li>{r['severity']} - {r['reason']} - {r['change']}</li>"

    html += "</ul>"

    with open(path, "w") as f:
        f.write(html)
