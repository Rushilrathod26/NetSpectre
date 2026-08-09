from rich.console import Console
from rich.table import Table

console = Console()


def show_scan_results(scan):
    table = Table(title="TCP Scan Results")

    table.add_column("PORT", style="cyan")
    table.add_column("STATE", style="green")
    table.add_column("SERVICE", style="yellow")
    table.add_column("VERSION", style="magenta")

    if not scan["open_ports"]:
        console.print("[red]No open ports found.[/red]")
        return

    for port in scan["open_ports"]:
        table.add_row(
            f"{port['port']}/tcp",
            "OPEN",
            port["service"],
            port.get("version", "Unknown")
        )

    console.print(table)

    console.print(f"\n[cyan]Open Ports :[/cyan] {len(scan['open_ports'])}")
    console.print(f"[cyan]Scan Time  :[/cyan] {scan['scan_time']:.2f} sec")
def show_udp_results(results):
    from rich.table import Table

    table = Table(title="UDP Scan Results")

    table.add_column("PORT", style="cyan")
    table.add_column("STATE", style="green")
    table.add_column("RESPONSE", style="yellow")

    found = False

    for item in results:
        if item["state"] in ("open", "open|filtered"):
            found = True

            response = (
                f"{item['response_time']} ms"
                if item["response_time"] is not None
                else "No response"
            )

            table.add_row(
                f"{item['port']}/udp",
                item["state"],
                response
            )

    if not found:
        console.print("[red]No UDP ports found.[/red]")
        return

    console.print(table)
    console.print(
        f"\n[cyan]UDP Results :[/cyan] "
        f"{sum(1 for x in results if x['state'] in ('open', 'open|filtered'))}"
    )
