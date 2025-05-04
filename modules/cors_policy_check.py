"""
Module: cors_policy_check.py
Checks the CORS policy by inspecting the Access-Control-Allow-Origin header.
"""
import requests
from rich.console import Console

console = Console()

def check_cors_policy(url):
    findings = []
    try:
        response = requests.get(url)
        cors = response.headers.get('Access-Control-Allow-Origin', None)
        if cors == '*':
            msg = "CORS policy is too permissive: Access-Control-Allow-Origin: *"
            console.print(f"[!] {msg}", style="red")
            findings.append(msg)
        elif cors:
            console.print(f"[i] CORS policy: Access-Control-Allow-Origin: {cors}")
        else:
            msg = "No CORS policy set."
            console.print(f"[i] {msg}")
            findings.append(msg)
    except Exception as e:
        msg = f"Error during CORS policy check: {e}"
        console.print(f"[!] {msg}", style="yellow")
        findings.append(msg)
    return findings
