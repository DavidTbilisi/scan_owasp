"""
Module: idor_check.py
Performs a basic IDOR (Insecure Direct Object Reference) check by attempting to access incremented/decremented object IDs and looking for unauthorized data exposure.
"""
import requests
from rich.console import Console
import re

console = Console()

def check_idor(url):
    findings = []
    # Try to identify an ID parameter in the URL
    match = re.search(r'(id|user|account|profile|order|doc|file|report)[=|/](\d+)', url, re.IGNORECASE)
    if not match:
        console.print("[i] No obvious ID parameter found for IDOR check.")
        return findings
    param, value = match.group(1), match.group(2)
    test_ids = [str(int(value) + 1), str(int(value) - 1)]
    for test_id in test_ids:
        test_url = re.sub(rf'({param}[=|/]){value}', rf'\1{test_id}', url)
        try:
            resp = requests.get(test_url)
            if resp.status_code == 200 and resp.text and resp.text != requests.get(url).text:
                msg = f"Possible IDOR: Able to access {param}={test_id} (status 200, different content)"
                console.print(f"[!] {msg}", style="bold red")
                findings.append({"detail": msg, "severity": "High"})
        except Exception:
            pass
    return findings
