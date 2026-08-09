import subprocess
import re

from core.mac_vendors import MAC_VENDORS


def get_mac_address(target):
    """
    Returns MAC Address from ARP table.
    """

    try:

        # Refresh ARP Cache
        subprocess.run(
            ["ping", "-c", "1", "-W", "1", target],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )

        result = subprocess.run(
            ["ip", "neigh", "show", target],
            capture_output=True,
            text=True
        )

        output = result.stdout

        match = re.search(
            r"lladdr\s+([0-9a-f:]{17})",
            output,
            re.IGNORECASE
        )

        if match:
            return match.group(1).upper()

        return None

    except Exception:
        return None


def get_mac_vendor(mac):

    if mac is None:
        return "Unknown"

    prefix = mac.upper()[:8]

    return MAC_VENDORS.get(prefix, "Unknown")
