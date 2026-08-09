from core.os_database import OS_DATABASE


def detect_os(fp, vendor="Unknown"):

    if fp is None:
        return None

    best = None
    best_score = -1

    for os in OS_DATABASE:

        score = 0

        # TTL Match
        if abs(fp["ttl"] - os["ttl"]) <= 5:
            score += 40

        # Window Match
        if fp["window"] == os["window"]:
            score += 40

        # Vendor Hints
        if vendor != "Unknown":

            if "VMware" in vendor and "VMware" in os["name"]:
                score += 20

            elif "Oracle" in vendor:
                score += 20

            elif "Apple" in vendor and "macOS" in os["name"]:
                score += 20

            elif "Cisco" in vendor and "Cisco" in os["name"]:
                score += 20

        if score > best_score:
            best_score = score
            best = os

    if best is None:
        return None

    return {
        "name": best["name"],
        "device": best["device"],
        "confidence": best_score
    }
