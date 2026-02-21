import datetime

def generate_html_report(risks, path="output/report.html"):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    html = f"""
    <html>
    <head>
        <title>ASM Security Report</title>
        <style>
            body {{ font-family: Arial, sans-serif; background-color: #f4f7f6; color: #333; margin: 40px; }}
            h1 {{ color: #2c3e50; border-bottom: 2px solid #3498db; padding-bottom: 10px; }}
            .summary {{ margin-bottom: 20px; font-weight: bold; }}
            table {{ width: 100%; border-collapse: collapse; margin-top: 20px; background: #fff; }}
            th, td {{ padding: 12px; text-align: left; border-bottom: 1px solid #ddd; }}
            th {{ background-color: #34495e; color: white; }}
            .HIGH {{ color: #e74c3c; font-weight: bold; }}
            .LOW {{ color: #27ae60; font-weight: bold; }}
            .MEDIUM {{ color: #f39c12; font-weight: bold; }}
        </style>
    </head>
    <body>
        <h1>🛡️ Attack Surface Management Report</h1>
        <p class="summary">Scan Completed: {timestamp}</p>
        
        <table>
            <tr>
                <th>Severity</th>
                <th>Reason</th>
                <th>Change Details (Host, Port, Service, Version)</th>
            </tr>
    """

    if not risks:
        html += "<tr><td colspan='3'>✅ No changes detected in the attack surface.</td></tr>"
    else:
        for r in risks:
            # Change tuple formatting to be cleaner
            change_details = f"{r['change'][0]}:{r['change'][1]} ({r['change'][2]} {r['change'][3]})"
            html += f"""
            <tr>
                <td class="{r['severity']}">{r['severity']}</td>
                <td>{r['reason']}</td>
                <td>{change_details}</td>
            </tr>
            """

    html += """
        </table>
    </body>
    </html>
    """

    with open(path, "w", encoding="utf-8") as f:
        f.write(html)