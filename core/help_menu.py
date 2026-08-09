"""
===========================================================
NetSpectre Help Menu
Author : Your Name
Version : 1.0.0
===========================================================
"""

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from core.constants import APP_NAME, VERSION

console = Console()


def show_help():

    title = Text()

    title.append(f"{APP_NAME} ", style="bold cyan")
    title.append(f"v{VERSION}", style="bold green")

    console.print(
        Panel.fit(
            title,
            subtitle="[yellow]Professional Network Reconnaissance Framework[/yellow]",
            border_style="cyan",
        )
    )

    console.print()

    console.print("[bold green]Yo Operator![/bold green] 😎")
    console.print("[white]Target do... magic nahi.[/white]")
    console.print("[dim]Main packets bhejta hu... future predict nahi karta. 😄[/dim]")

    console.print()

    usage = Table(show_header=False, box=None)

    usage.add_row("[cyan]Usage[/cyan]")
    usage.add_row("[green]netspectre -t <target> [options][/green]")

    console.print(usage)

    console.print()

    basic = Table(title="Basic Options", border_style="cyan")

    basic.add_column("Option", style="green")
    basic.add_column("Description", style="white")

    basic.add_row("-t, --target", "Target IP Address or Domain")
    basic.add_row("-p, --ports", "Port Range (Example : 1-1000)")
    basic.add_row("-A", "Aggressive Scan")
    basic.add_row("-U", "UDP Scan")
    basic.add_row("-O", "OS Detection")
    basic.add_row("-v", "Verbose Output")
    basic.add_row("--version", "Display Version")
    basic.add_row("-h, --help", "Display Help Menu")

    console.print(basic)

    console.print()

    enum = Table(title="Recon Modules", border_style="magenta")

    enum.add_column("Module", style="cyan")
    enum.add_column("Description", style="white")

    enum.add_row("--dns", "DNS Enumeration")
    enum.add_row("--whois", "WHOIS Lookup")
    enum.add_row("--headers", "HTTP Header Analysis")
    enum.add_row("--robots", "robots.txt Enumeration")
    enum.add_row("--ssl", "SSL Information")
    enum.add_row("--tech", "Technology Detection")

    console.print(enum)

    console.print()

    report = Table(title="Report Formats", border_style="yellow")

    report.add_column("Format")
    report.add_column("Description")

    report.add_row("txt", "Plain Text Report")
    report.add_row("json", "Machine Readable")
    report.add_row("html", "Beautiful HTML Report")

    console.print(report)

    console.print()

    examples = Table(title="Examples", border_style="green")

    examples.add_column("Command")

    examples.add_row("netspectre -t google.com")
    examples.add_row("netspectre -t scanme.nmap.org -A")
    examples.add_row("netspectre -t 192.168.1.10 -p 1-65535")
    examples.add_row("netspectre -t example.com --dns")
    examples.add_row("netspectre -t example.com --report html")

    console.print(examples)

    console.print()

    console.print(
        Panel.fit(
            "[bold yellow]⚠ Legal Warning[/bold yellow]\n\n"
            "Scan only systems you own or have explicit permission to test.\n"
            "Unauthorized scanning can create legal problems faster than open ports.",
            border_style="red",
        )
    )

    console.print()

    quotes = [
        "Packets don't lie. People do.",
        "Recon first. Exploit later.",
        "Every open port has a story.",
        "Curiosity is good. Unauthorized access isn't.",
        "No target. No scan. Simple."
    ]

    import random

    console.print(
        Panel.fit(
            f"[bold cyan]Quote of the Run[/bold cyan]\n\n"
            f"[green]{random.choice(quotes)}[/green]",
            border_style="blue",
        )
    )

    console.print()

    console.print("[bold green]Happy Recon! 🚀[/bold green]")
