import subprocess


def whois_lookup(target):
    try:
        result = subprocess.run(
            ["whois", target],
            capture_output=True,
            text=True,
            timeout=15
        )

        if result.returncode != 0:
            return None

        output = result.stdout

        data = {
            "domain": None,
            "registry_id": None,
            "whois_server": None,
            "registrar": None,
            "registrar_url": None,
            "registrar_iana_id": None,
            "creation_date": None,
            "updated_date": None,
            "expiry_date": None,
            "domain_status": [],
            "name_servers": [],
            "dnssec": None,
            "dnssec_ds_data": None,
            "organisation": None,
            "source": None
        }

        for line in output.splitlines():
            line = line.strip()

            if not line:
                continue

            # Ignore WHOIS comments
            if line.startswith("%"):
                continue

            lower = line.lower()

            # Domain
            if lower.startswith("domain name:"):
                data["domain"] = line.split(":", 1)[1].strip()

            # Registry ID
            elif lower.startswith("registry domain id:"):
                data["registry_id"] = line.split(":", 1)[1].strip()

            # WHOIS Server
            elif lower.startswith("registrar whois server:"):
                data["whois_server"] = line.split(":", 1)[1].strip()

            # Registrar
            elif lower.startswith("registrar:"):
                data["registrar"] = line.split(":", 1)[1].strip()

            # Registrar URL
            elif lower.startswith("registrar url:"):
                data["registrar_url"] = line.split(":", 1)[1].strip()

            # Registrar IANA ID
            elif lower.startswith("registrar iana id:"):
                data["registrar_iana_id"] = line.split(":", 1)[1].strip()

            # Creation Date
            elif lower.startswith("creation date:"):
                data["creation_date"] = line.split(":", 1)[1].strip()

            # Updated Date
            elif lower.startswith("updated date:"):
                data["updated_date"] = line.split(":", 1)[1].strip()

            # Expiry Date
            elif lower.startswith("registry expiry date:"):
                data["expiry_date"] = line.split(":", 1)[1].strip()

            # Domain Status
            elif lower.startswith("domain status:"):
                status = line.split(":", 1)[1].strip()

                if status:
                    data["domain_status"].append(status)

            # Name Server
            elif lower.startswith("name server:"):
                nameserver = line.split(":", 1)[1].strip()

                if nameserver and nameserver not in data["name_servers"]:
                    data["name_servers"].append(nameserver)

            # DNSSEC
            elif lower.startswith("dnssec:"):
                data["dnssec"] = line.split(":", 1)[1].strip()

            # DNSSEC DS Data
            elif lower.startswith("dnssec ds data:"):
                data["dnssec_ds_data"] = line.split(":", 1)[1].strip()

            # IANA Organisation
            elif lower.startswith("organisation:"):
                data["organisation"] = line.split(":", 1)[1].strip()

            # IANA Source
            elif lower.startswith("source:"):
                data["source"] = line.split(":", 1)[1].strip()

        return data

    except Exception:
        return None
