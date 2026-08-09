"""
=========================================================
 NetSpectre
 Professional Network Reconnaissance Framework

 Author  : Your Name
 Version : 1.0.0
=========================================================
"""

import sys
import time
from banner import show_banner
from cli import parse_arguments
from core.logger import logger
from core.help_menu import show_help
from core.constants import APP_NAME, VERSION
from modules.service_detect import detect_service

def main():
    # Display Banner
    show_banner()

    logger.info("NetSpectre Started")

    # Parse CLI Arguments
    args = parse_arguments()
    # Start total scan timer
    scan_start_time = time.perf_counter()

    # ==============================
    # Top Ports Shortcut
    # ==============================
    if args.top_ports:

        if args.top_ports is None:
            args.ports = "1-1000"

        elif args.top_ports == 1000:
            args.ports = "1-1000"

        else:
            print("[ERROR] Supported values are only:")
            print("   --top-ports 100")
            print("   --top-ports 1000")
            sys.exit(1)

    # Version
    if getattr(args, "version", False):
        print(f"{APP_NAME} v{VERSION}")
        sys.exit(0)
    # Help
    if getattr(args, "help", False):
        show_help()
        sys.exit(0)

    # No Target
    if not getattr(args, "target", None):
        print("\n[!] No target specified.\n")
        print("Main psychic nahi hu. 🔮")
        print("Target do... phir packets bhejte hain.\n")
        print("Try:")
        print("  python3 netspectre.py -t scanme.nmap.org")
        print("  python3 netspectre.py --help\n")
        sys.exit(1)

    # Target Received
    target = args.target

    logger.info(f"Target Selected : {target}")

    print("\n══════════════════════════════════════════════")
    print(" Recon Mode Activated")
    print("══════════════════════════════════════════════")
    print(f" Target   : {target}")
    print(" Status   : READY")
    print(" Mission  : Enumeration")
    print("══════════════════════════════════════════════\n")

    print("Recon mode engaged.")
    print("Packets are leaving the keyboard... 🚀")
    print("Good luck, Operator.\n")


    # ==============================
    # Host Discovery
    # ==============================
    from modules.host_discovery import host_discovery

    if args.Pn:
        print("[INFO] -Pn enabled. Skipping Host Discovery.\n")
    else:
        result = host_discovery(target)

        if result is None:
            sys.exit(1)

        if not result["alive"]:
            print("\n[WARNING] Host discovery failed.")
            print("Use -Pn to skip host discovery.")
            sys.exit(1)


    # ==============================
    # TCP Scan
    # ==============================

    scan = None

    udp_results = []
    dns_info = None
    whois_info = None
    header_info = None
    robots_info = None
    ssl_info = None
    tech_info = None
    os_info = None
    fp = None
    mac = None
    vendor = None

    if (
        not args.udp
        and not args.dns
        and not args.whois
        and not args.os_detection
       and not args.headers
       and not args.robots
    and not args.ssl
    and not args.tech
    ) or args.aggressive:

        from modules.go_scanner import run_go_scanner

        print("\n[INFO] Starting TCP Scan...\n")

        scan = run_go_scanner(target, args.ports)


    # ==============================
    # UDP Scan
    # ==============================

    if args.udp or args.aggressive:
        from modules.udp_scan import scan_udp
        from modules.output import show_udp_results
        from core.services import get_udp_service_name

        print("\n[INFO] Starting UDP Scan...\n")

        udp_ports = [
            53, 67, 68, 69, 123,
            137, 138, 161, 162,
            500, 514, 520, 631
        ]

        udp_results = scan_udp(target, udp_ports)

        for item in udp_results:
            item["service"] = get_udp_service_name(item["port"])

        show_udp_results(udp_results)



    # ==============================
    # DNS Enumeration
    # ==============================
    if args.dns or args.aggressive:

        from modules.dns_enum import dns_lookup

        print("\n════════════════════════════════════")
        print(" DNS ENUMERATION")
        print("════════════════════════════════════")

        dns_info = dns_lookup(target)

        if dns_info:
            print(f"Hostname    : {dns_info['hostname']}")
            print(f"IP Address  : {dns_info['ip']}")
            print(f"Reverse DNS : {dns_info['reverse_dns']}")
        else:
            print("DNS lookup failed.")

        print("════════════════════════════════════\n")



    # ==============================
    # WHOIS Enumeration
    # ==============================
    if args.whois or args.aggressive:

        from modules.whois_enum import whois_lookup

        print("\n════════════════════════════════════")
        print(" WHOIS ENUMERATION")
        print("════════════════════════════════════")

        whois_info = whois_lookup(target)
        if whois_info:
            print(f"Domain          : {whois_info.get('domain') or 'Unknown'}")
            print(f"Registry ID     : {whois_info.get('registry_id') or 'Unknown'}")
            print(f"WHOIS Server    : {whois_info.get('whois_server') or 'Unknown'}")
            print(f"Registrar       : {whois_info.get('registrar') or 'Unknown'}")
            print(f"Registrar URL   : {whois_info.get('registrar_url') or 'Unknown'}")
            print(f"Registrar IANA  : {whois_info.get('registrar_iana_id') or 'Unknown'}")
            print(f"Created         : {whois_info.get('creation_date') or 'Unknown'}")
            print(f"Updated         : {whois_info.get('updated_date') or 'Unknown'}")
            print(f"Expires         : {whois_info.get('expiry_date') or 'Unknown'}")

            statuses = whois_info.get('domain_status', [])
            if statuses:
                print("Domain Status:")
                for status in statuses:
                    print(f"  • {status}")

            name_servers = whois_info.get('name_servers', [])
            if name_servers:
                print("Name Servers:")
                for server in name_servers:
                    print(f"  • {server}")

            print(f"DNSSEC          : {whois_info.get('dnssec') or 'Unknown'}")
            print(f"DNSSEC DS Data  : {whois_info.get('dnssec_ds_data') or 'Unknown'}")
            print(f"Organisation    : {whois_info.get('organisation') or 'Unknown'}")
            print(f"Source          : {whois_info.get('source') or 'Unknown'}")
        else:
            print("WHOIS lookup failed.")
        print("════════════════════════════════════\n")

    # ==============================
    # HTTP Header Analysis
    # ==============================
    if args.headers or args.aggressive:

        from modules.headers import get_http_headers

        print("\n════════════════════════════════════")
        print(" HTTP HEADER ANALYSIS")
        print("════════════════════════════════════")

        header_info = get_http_headers(target)

        if header_info:
            print(f"URL         : {header_info['url']}")
            print(f"Status Code : {header_info['status_code']}")

            print("\nHeaders:")

            for key, value in header_info["headers"].items():
                    print(f"{key}: {value}")
        else:
            print("HTTP header lookup failed.")

        print("════════════════════════════════════\n")



    # ==============================
    # Robots.txt Enumeration
    # ==============================
    if args.robots or args.aggressive:
    
        from modules.robots import get_robots
    
        print("\n════════════════════════════════════")
        print(" ROBOTS.TXT ENUMERATION")
        print("════════════════════════════════════")
    
        robots_info = get_robots(target)
    
        if robots_info:
            print(f"URL         : {robots_info['url']}")
            print(f"Status Code : {robots_info['status_code']}")
    
            if robots_info["entries"]:
                print("\nDiscovered Entries:")
    
                for entry in robots_info["entries"]:
                    print(f"  • {entry}")
            else:
                print("\nNo robots.txt directives found.")
        else:
            print("robots.txt lookup failed.")
    
        print("════════════════════════════════════\n")


    # ==============================
    # SSL Information
    # ==============================
    if args.ssl or args.aggressive:
    
        from modules.ssl_info import get_ssl_info
    
        print("\n════════════════════════════════════")
        print(" SSL/TLS INFORMATION")
        print("════════════════════════════════════")
    
        ssl_info = get_ssl_info(target)
    
        if "error" in ssl_info:
            print(f"SSL lookup failed : {ssl_info['error']}")
        else:
            print(f"Hostname   : {ssl_info['hostname']}")
            print(f"TLS Version: {ssl_info['tls_version']}")
            print(f"Cipher     : {ssl_info['cipher']}")
            print(f"Subject    : {ssl_info['subject']}")
            print(f"Issuer     : {ssl_info['issuer']}")
            print(f"Valid From : {ssl_info['valid_from']}")
            print(f"Valid Until: {ssl_info['valid_until']}")
    
        print("════════════════════════════════════\n")
        # ==============================
        # Technology Detection
    # ==============================
    if args.tech or args.aggressive:

        from modules.tech_detect import detect_technologies

        print("\n════════════════════════════════════")
        print(" TECHNOLOGY DETECTION")
        print("════════════════════════════════════")

        tech_info = detect_technologies(target)

        if "error" in tech_info:
            print(f"Technology detection failed : {tech_info['error']}")

        else:
            print(f"URL         : {tech_info['url']}")
            print(f"Status Code : {tech_info['status_code']}")

            if tech_info["technologies"]:
                print("\nDetected Technologies:")

                for tech in tech_info["technologies"]:
                    print(f"  • {tech}")

            else:
                print("\nNo technology indicators detected.")

        print("════════════════════════════════════\n")


    # ==============================
    # OS Detection
    # ==============================
    if args.os_detection or args.aggressive:

        from modules.fingerprint import collect_fingerprint
        from modules.os_detect import detect_os
        from modules.mac_detect import get_mac_address, get_mac_vendor

        fp = collect_fingerprint(target)

        mac = get_mac_address(target)
        vendor = get_mac_vendor(mac)

        os_info = detect_os(fp, vendor)

        print("\n════════════════════════════════════")
        print(" OS DETECTION")
        print("════════════════════════════════════")

        if os_info:

            print(f"Operating System : {os_info['name']}")
            print(f"Device Type      : {os_info['device']}")
            print(f"Confidence       : {os_info['confidence']}%")

            print(f"MAC Address      : {mac}")
            print(f"MAC Vendor       : {vendor}")
    
            print(f"TTL              : {fp['ttl']}")
            print(f"TCP Window       : {fp['window']}")
            print(f"DF Bit           : {'Set' if fp['df'] else 'Not Set'}")

        else:
            print("Operating System : Unknown")

            print("════════════════════════════════════\n")






    # ==============================
    # TCP Scan Results
    # ==============================

    if scan is not None:

        if not scan["open_ports"]:
            print("No open ports found.")
        else:
            print("[INFO] Running Service Version Detection...\n")

            for port in scan["open_ports"]:
                version = detect_service(target, port["port"])

                if version:
                    port["version"] = version.strip()
                else:
                    port["version"] = "Unknown"

        from modules.output import show_scan_results
        show_scan_results(scan)

    # ==============================
    # Report Generation
    # ==============================

    if args.report:

        from modules.report import generate_report

        report_data = {
            "tcp_scan": scan,
            "udp_scan": udp_results,
            "dns": dns_info,
            "whois": whois_info,
            "http_headers": header_info,
            "robots": robots_info,
            "ssl": ssl_info,
            "technology": tech_info,
            "os_detection": {
                "os": os_info,
                "mac_address": mac,
                "mac_vendor": vendor,
                "fingerprint": fp
            }
        }

        report_file = generate_report(
            report_data,
            args.report,
            target
        )

        if report_file:
            print(
                f"\n[INFO] {args.report.upper()} report saved: "
                f"{report_file}"
            )

    # ==============================
    # Total Scan Time
    # ==============================

    total_scan_time = time.perf_counter() - scan_start_time

    print("\n════════════════════════════════════")
    print(" SCAN SUMMARY")
    print("════════════════════════════════════")
    print(f"Target      : {target}")
    print(f"Scan Time   : {total_scan_time:.2f} sec")
    print("Status      : Completed")
    print("════════════════════════════════════\n")


if __name__ == "__main__":
    main()
