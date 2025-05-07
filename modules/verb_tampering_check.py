"""
Module: verb_tampering_check.py
Performs a basic HTTP verb tampering check by sending requests with different HTTP methods (GET, POST, PUT, DELETE) and looking for unexpected or risky behavior.
"""
import requests
from rich.console import Console

console = Console()

def check_verb_tampering(url):
    findings = []
    methods = ['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS']
    for method in methods:
        try:
            resp = requests.request(method, url)
            if method not in ['GET', 'OPTIONS'] and resp.status_code in [200, 201, 202, 204]:
                msg = f"HTTP verb tampering: {method} allowed on {url} (status {resp.status_code})"
                console.print(f"[!] {msg}", style="bold red")
                findings.append({"detail": msg, "severity": "High"})
            elif method == 'OPTIONS' and 'allow' in resp.headers:
                msg = f"OPTIONS response: {resp.headers['allow']}"
                console.print(f"[i] {msg}")
        except Exception:
            pass
    return findings
