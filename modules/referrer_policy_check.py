"""
Module: referrer_policy_check.py
Checks for the Referrer-Policy header to ensure privacy.
"""
import requests
from rich.console import Console

console = Console()

def check_referrer_policy(url):
    findings = []
    try:
        response = requests.get(url)
        referrer_policy = response.headers.get('Referrer-Policy', None)
        if not referrer_policy:
            msg = "Referrer-Policy header is missing!"
            console.print(f"[!] {msg}", style="red")
            findings.append(msg)
        else:
            console.print(f"[i] Referrer-Policy: {referrer_policy}")
    except Exception as e:
        msg = f"Error during Referrer-Policy check: {e}"
        console.print(f"[!] {msg}", style="yellow")
        findings.append(msg)
    return findings
