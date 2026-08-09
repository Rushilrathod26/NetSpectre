"""
=========================================================
 NetSpectre
 Module : Validator

 Description:
 Validates targets (IP / Domain) and port ranges.

 Author  : Your Name
 Version : 1.0.0
=========================================================
"""

import ipaddress
import re


DOMAIN_REGEX = re.compile(
    r"^(?!-)(?:[A-Za-z0-9-]{1,63}\.)+[A-Za-z]{2,63}$"
)


def is_valid_ip(target: str) -> bool:
    """
    Returns True if target is a valid IPv4 or IPv6 address.
    """
    try:
        ipaddress.ip_address(target)
        return True
    except ValueError:
        return False


def is_valid_domain(target: str) -> bool:
    """
    Returns True if target is a valid domain name.
    """
    return bool(DOMAIN_REGEX.fullmatch(target))


def validate_target(target: str) -> bool:
    """
    Validates whether target is a valid IP or Domain.
    """
    return is_valid_ip(target) or is_valid_domain(target)


def validate_port_range(port_range: str) -> bool:
    """
    Validates port range.
    Example:
        80
        1-1000
    """

    if port_range.isdigit():
        port = int(port_range)
        return 1 <= port <= 65535

    if "-" not in port_range:
        return False

    start, end = port_range.split("-", 1)

    if not start.isdigit() or not end.isdigit():
        return False

    start = int(start)
    end = int(end)

    if start < 1 or end > 65535:
        return False

    if start > end:
        return False

    return True
