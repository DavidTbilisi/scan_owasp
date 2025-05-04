"""
Module: xss_check.py
Performs a basic reflected XSS check by injecting a harmless script and checking if it is reflected in the response.
"""
import requests
from rich.console import Console

console = Console()

def check_xss(url):
    # Add a simple XSS payload to the URL
    payload = '<script>alert(1)</script>'
    test_url = url + (f"?q={payload}" if '?' not in url else f"&q={payload}")
    try:
        response = requests.get(test_url)
        if payload in response.text:
            console.print("[!] Possible reflected XSS vulnerability detected!", style="bold red")
        else:
            console.print("[+] No obvious reflected XSS vulnerability detected.", style="green")
    except Exception as e:
        console.print(f"[!] Error during XSS check: {e}", style="yellow")
