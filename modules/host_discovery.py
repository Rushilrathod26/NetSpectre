"""
=========================================================
 NetSpectre
 Module : Host Discovery

 Description:
 Resolves target hostname and performs basic TCP host discovery.

 Author  : Your Name
 Version : 1.0.0
=========================================================
"""

import socket
import time
from rich.console import Console
from rich.table import Table

console = Console()


def host_discovery(target: str, timeout: float = 3.0):
    """
    Resolve target and perform basic TCP connectivity check.
    Returns:
        {
            "target": "...",
            "ip": "...",
            "alive": True/False,
            "response_time": xx.xx
        }
    """

    try:
        ip = socket.gethostbyname(target)
    except socket.gaierror:
        console.print(f"[bold red][-][/bold red] Unable to resolve [cyan]{target}[/cyan]")
        console.print("[yellow]DNS replied:[/yellow] 'I have no idea who you're talking about.' 😅")
        return None

    start = time.perf_counter()

    alive = False

    # Common ports used only for discovery
    discovery_ports = [
    	20,21,22,23,25,
    	53,67,68,
    	80,110,111,123,
    	135,137,138,139,
    	143,161,162,
    	389,443,445,
    	465,587,
    	993,995,
    	1433,1521,
    	2049,3306,
    	3389,
    	5432,
    	5900,
    	6379,
    	8080,
    	8443,
    	9000,
    	9200,
    	27017
    ]
    for port in discovery_ports:
        try:
            sock = socket.create_connection((ip, port), timeout=timeout)
            sock.close()
            alive = True
            break
        except Exception:
            continue

    elapsed = round((time.perf_counter() - start) * 1000, 2)

    table = Table(title="HOST DISCOVERY", border_style="cyan")

    table.add_column("Field", style="green", no_wrap=True)
    table.add_column("Value", style="white")

    table.add_row("Target", target)
    table.add_row("Resolved IP", ip)
    table.add_row("Status", "ALIVE ✅" if alive else "NO RESPONSE ❌")
    table.add_row("Response Time", f"{elapsed} ms")

    console.print(table)

    if alive:
        console.print("\n[bold green][+][/bold green] Recon mode engaged.")
        console.print("[cyan]Packets are leaving the keyboard...[/cyan]")
        console.print("[green]Moving to TCP Scanner.[/green]\n")
    else:
        console.print("\n[bold yellow][!][/bold yellow] Host didn't answer on discovery ports.")
        console.print("[yellow]Maybe it's filtered... maybe it's sleeping... maybe it's just ignoring us. 😄[/yellow]")
        console.print("[cyan]Use -Pn in future versions to continue anyway.[/cyan]\n")

    return {
        "target": target,
        "ip": ip,
        "alive": alive,
        "response_time": elapsed,
    }
