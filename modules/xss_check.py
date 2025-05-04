"""
Module: xss_check.py
Performs a basic reflected XSS check by injecting a harmless script and checking if it is reflected in the response.
"""
import requests
from rich.console import Console

console = Console()

def check_xss(url):
    findings = []
    # Add a simple XSS payload to the URL
    payload = '<script>alert(1)</script>'
    test_url = url + (f"?q={payload}" if '?' not in url else f"&q={payload}")
    try:
        response = requests.get(test_url)
        if payload in response.text:
            msg = "Possible reflected XSS vulnerability detected!"
            console.print(f"[!] {msg}", style="bold red")
            findings.append(msg)
        else:
            console.print("[+] No obvious reflected XSS vulnerability detected.", style="green")
    except Exception as e:
        msg = f"Error during XSS check: {e}"
        console.print(f"[!] {msg}", style="yellow")
        findings.append(msg)
    return findings
