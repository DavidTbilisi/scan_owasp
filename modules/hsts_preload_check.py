"""
Module: hsts_preload_check.py
Checks if Strict-Transport-Security is set with preload, max-age, and includeSubDomains.
"""
import requests
from rich.console import Console

console = Console()

def check_hsts_preload(url):
    try:
        response = requests.get(url)
        hsts = response.headers.get('Strict-Transport-Security', None)
        if not hsts:
            console.print("[!] Strict-Transport-Security header is missing!", style="red")
            return
        if 'preload' in hsts and 'max-age=' in hsts and 'includesubdomains' in hsts.lower():
            console.print(f"[+] HSTS is properly configured for preload: {hsts}", style="green")
        else:
            console.print(f"[!] HSTS header is present but not fully configured for preload: {hsts}", style="yellow")
    except Exception as e:
        console.print(f"[!] Error during HSTS preload check: {e}", style="yellow")
