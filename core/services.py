SERVICES = {
    20: "ftp-data",
    21: "ftp",
    22: "ssh",
    23: "telnet",
    25: "smtp",
    53: "dns",
    67: "dhcp",
    68: "dhcp",
    69: "tftp",
    80: "http",
    110: "pop3",
    111: "rpcbind",
    123: "ntp",
    135: "msrpc",
    139: "netbios-ssn",
    143: "imap",
    161: "snmp",
    389: "ldap",
    443: "https",
    445: "microsoft-ds",
    465: "smtps",
    514: "syslog",
    587: "submission",
    631: "ipp",
    993: "imaps",
    995: "pop3s",
    1433: "mssql",
    1521: "oracle",
    2049: "nfs",
    3306: "mysql",
    3389: "rdp",
    5432: "postgresql",
    5900: "vnc",
    6379: "redis",
    8080: "http-proxy",
    8443: "https-alt",
    9000: "php-fpm",
    9200: "elasticsearch",
    27017: "mongodb"
}


def get_service_name(port):
    return SERVICES.get(port, "unknown")
def get_udp_service_name(port):
    udp_services = {
        53: "DNS",
        67: "DHCP Server",
        68: "DHCP Client",
        69: "TFTP",
        123: "NTP",
        137: "NetBIOS Name Service",
        138: "NetBIOS Datagram",
        161: "SNMP",
        162: "SNMP Trap",
        500: "IKE",
        514: "Syslog",
        520: "RIP",
        631: "IPP"
    }

    return udp_services.get(port, "Unknown")
