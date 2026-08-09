import argparse

from core.constants import APP_NAME


def parse_arguments():

    parser = argparse.ArgumentParser(
        prog=APP_NAME,
        description="Professional Network Reconnaissance Framework",
        add_help=False
    )

    parser.add_argument("-t", "--target", help="Target IP Address or Domain")

    parser.add_argument(
    	"-p",
    	"--ports",
    	default="1-1000",
    	help="Port Range (default: 1-1000)"
    )
    parser.add_argument("-A", "--aggressive", action="store_true")

    parser.add_argument("-U", "--udp", action="store_true", help="Enable UDP scan")

    parser.add_argument(
    	"--whois",
    	action="store_true",
    	help="WHOIS information lookup"
    )

    parser.add_argument("--dns", action="store_true", help="Perform DNS enumeration")

    parser.add_argument("-O", "--os-detection", dest="os_detection", action="store_true",
                    help="Enable OS detection")

    parser.add_argument(
    	"--headers",
    	action="store_true",
    	help="HTTP Header Analysis"
    )

    parser.add_argument(
    	"--robots",
    	action="store_true",
    	help="robots.txt Enumeration"
    )

    parser.add_argument(
    	"--ssl",
    	action="store_true",
    	help="SSL/TLS Certificate Information"
    )

    parser.add_argument(
    	"--tech",
    	action="store_true",
    	help="Technology Detection"
    )

    parser.add_argument(
    	"--report",
    	choices=["txt", "json", "html"],
    	help="Generate scan report"
    )

    parser.add_argument("-v", "--verbose", action="store_true")

    parser.add_argument("-Pn",action="store_true",help="Skip host discovery")

    parser.add_argument ("--top-ports",type=int,help="Scan the top N most common ports")

    parser.add_argument("-h", "--help", action="store_true")

    parser.add_argument("--version", action="store_true")

    return parser.parse_args()
