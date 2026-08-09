import json
from datetime import datetime


def generate_report(report_data, report_format, target):

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    display_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    tcp_scan = report_data.get("tcp_scan")
    udp_scan = report_data.get("udp_scan", [])
    dns_info = report_data.get("dns")
    whois_info = report_data.get("whois")
    header_info = report_data.get("http_headers")
    robots_info = report_data.get("robots")
    ssl_info = report_data.get("ssl")
    tech_info = report_data.get("technology")
    os_info = report_data.get("os_detection")

    report = {
        "tool": "NetSpectre",
        "version": "1.0.0",
        "target": target,
        "scan_time": display_time,
        "results": report_data
    }

    # ==============================
    # JSON REPORT
    # ==============================

    if report_format == "json":

        filename = f"netspectre_report_{timestamp}.json"

        with open(filename, "w") as f:
            json.dump(report, f, indent=4, default=str)

    # ==============================
    # TXT REPORT
    # ==============================

    elif report_format == "txt":

        filename = f"netspectre_report_{timestamp}.txt"

        with open(filename, "w") as f:

            f.write("=" * 60 + "\n")
            f.write("              NETSPECTRE SCAN REPORT\n")
            f.write("=" * 60 + "\n\n")

            f.write(f"Target      : {target}\n")
            f.write(f"Scan Time   : {display_time}\n")
            f.write("Tool        : NetSpectre v1.0.0\n\n")

            # TCP
            f.write("-" * 60 + "\n")
            f.write("TCP SCAN RESULTS\n")
            f.write("-" * 60 + "\n")

            open_ports = []

            if isinstance(tcp_scan, dict):
                open_ports = tcp_scan.get("open_ports", [])

            f.write(f"Open Ports  : {len(open_ports)}\n\n")

            if open_ports:
                for port in open_ports:
                    f.write(f"Port        : {port.get('port', 'Unknown')}/tcp\n")
                    f.write(f"Service     : {port.get('service', 'Unknown')}\n")
                    f.write(f"Version     : {port.get('version', 'Unknown')}\n")
                    f.write("-" * 60 + "\n")
            else:
                f.write("No open TCP ports detected.\n")

            # UDP
            f.write("\n" + "-" * 60 + "\n")
            f.write("UDP SCAN RESULTS\n")
            f.write("-" * 60 + "\n")

            if udp_scan:
                for item in udp_scan:
                    f.write(
                        f"Port        : {item.get('port', 'Unknown')}/udp\n"
                    )
                    f.write(
                        f"State       : {item.get('state', 'Unknown')}\n"
                    )
                    f.write(
                        f"Service     : {item.get('service', 'Unknown')}\n"
                    )
                    f.write("-" * 60 + "\n")
            else:
                f.write("No UDP results.\n")

            # DNS
            f.write("\n" + "-" * 60 + "\n")
            f.write("DNS ENUMERATION\n")
            f.write("-" * 60 + "\n")

            if dns_info:
                f.write(json.dumps(dns_info, indent=4, default=str))
                f.write("\n")
            else:
                f.write("No DNS information.\n")

            # WHOIS
            f.write("\n" + "-" * 60 + "\n")
            f.write("WHOIS ENUMERATION\n")
            f.write("-" * 60 + "\n")

            if whois_info:
                f.write(str(whois_info))
                f.write("\n")
            else:
                f.write("No WHOIS information.\n")

            # HTTP HEADERS
            f.write("\n" + "-" * 60 + "\n")
            f.write("HTTP HEADER ANALYSIS\n")
            f.write("-" * 60 + "\n")

            if header_info:
                f.write(json.dumps(header_info, indent=4, default=str))
                f.write("\n")
            else:
                f.write("No HTTP header information.\n")

            # ROBOTS
            f.write("\n" + "-" * 60 + "\n")
            f.write("ROBOTS.TXT ENUMERATION\n")
            f.write("-" * 60 + "\n")

            if robots_info:
                f.write(json.dumps(robots_info, indent=4, default=str))
                f.write("\n")
            else:
                f.write("No robots.txt information.\n")

            # SSL
            f.write("\n" + "-" * 60 + "\n")
            f.write("SSL INFORMATION\n")
            f.write("-" * 60 + "\n")

            if ssl_info:
                f.write(json.dumps(ssl_info, indent=4, default=str))
                f.write("\n")
            else:
                f.write("No SSL information.\n")

            # TECHNOLOGY
            f.write("\n" + "-" * 60 + "\n")
            f.write("TECHNOLOGY DETECTION\n")
            f.write("-" * 60 + "\n")

            if tech_info:
                f.write(json.dumps(tech_info, indent=4, default=str))
                f.write("\n")
            else:
                f.write("No technology information.\n")

            # OS
            f.write("\n" + "-" * 60 + "\n")
            f.write("OS DETECTION\n")
            f.write("-" * 60 + "\n")

            if os_info:
                f.write(json.dumps(os_info, indent=4, default=str))
                f.write("\n")
            else:
                f.write("No OS detection information.\n")

            f.write("\n" + "=" * 60 + "\n")
            f.write("                 END OF REPORT\n")
            f.write("=" * 60 + "\n")

    # ==============================
    # HTML REPORT
    # ==============================

    elif report_format == "html":

        filename = f"netspectre_report_{timestamp}.html"

        open_ports = []

        if isinstance(tcp_scan, dict):
            open_ports = tcp_scan.get("open_ports", [])

        rows = ""

        for port in open_ports:

            rows += f"""
            <tr>
                <td>{port.get('port', 'Unknown')}/tcp</td>
                <td>{port.get('service', 'Unknown')}</td>
                <td>{port.get('version', 'Unknown')}</td>
            </tr>
            """

        if not rows:
            rows = """
            <tr>
                <td colspan="3">No open TCP ports detected.</td>
            </tr>
            """

        html = f"""
<!DOCTYPE html>
<html>
<head>

<meta charset="UTF-8">

<title>NetSpectre Scan Report</title>

<style>

body {{
    font-family: Arial, sans-serif;
    background: #f4f6f8;
    margin: 0;
    padding: 40px;
}}

.container {{
    max-width: 1100px;
    margin: auto;
    background: white;
    padding: 35px;
    border-radius: 10px;
}}

h1 {{
    margin-bottom: 5px;
}}

.subtitle {{
    color: #666;
    margin-bottom: 30px;
}}

.card {{
    background: #f8f9fa;
    padding: 18px;
    border-radius: 8px;
    margin-bottom: 15px;
}}

table {{
    width: 100%;
    border-collapse: collapse;
}}

th, td {{
    padding: 12px;
    border-bottom: 1px solid #ddd;
    text-align: left;
}}

pre {{
    background: #f4f4f4;
    padding: 15px;
    border-radius: 6px;
    overflow-x: auto;
}}

.section {{
    margin-top: 35px;
}}

.footer {{
    margin-top: 30px;
    color: #777;
    font-size: 13px;
}}

</style>

</head>

<body>

<div class="container">

<h1>NetSpectre Scan Report</h1>

<div class="subtitle">
Professional Network Reconnaissance Framework
</div>

<div class="card">
<strong>Target</strong>
{target}
</div>

<div class="card">
<strong>Scan Time</strong>
{display_time}
</div>

<div class="card">
<strong>TCP Open Ports</strong>
{len(open_ports)}
</div>


<div class="section">

<h2>TCP Scan Results</h2>

<table>

<thead>
<tr>
<th>Port</th>
<th>Service</th>
<th>Version</th>
</tr>
</thead>

<tbody>
{rows}
</tbody>

</table>

</div>


<div class="section">

<h2>UDP Scan</h2>

<pre>{json.dumps(udp_scan, indent=4, default=str)}</pre>

</div>


<div class="section">

<h2>DNS Enumeration</h2>

<pre>{json.dumps(dns_info, indent=4, default=str)}</pre>

</div>


<div class="section">

<h2>WHOIS Enumeration</h2>

<pre>{str(whois_info) if whois_info else "No WHOIS information."}</pre>

</div>


<div class="section">

<h2>HTTP Headers</h2>

<pre>{json.dumps(header_info, indent=4, default=str)}</pre>

</div>


<div class="section">

<h2>Robots.txt</h2>

<pre>{json.dumps(robots_info, indent=4, default=str)}</pre>

</div>


<div class="section">

<h2>SSL Information</h2>

<pre>{json.dumps(ssl_info, indent=4, default=str)}</pre>

</div>


<div class="section">

<h2>Technology Detection</h2>

<pre>{json.dumps(tech_info, indent=4, default=str)}</pre>

</div>


<div class="section">

<h2>OS Detection</h2>

<pre>{json.dumps(os_info, indent=4, default=str)}</pre>

</div>


<div class="footer">
Generated by NetSpectre v1.0.0
</div>

</div>

</body>
</html>
"""

        with open(filename, "w") as f:
            f.write(html)

    else:
        return None

    return filename
