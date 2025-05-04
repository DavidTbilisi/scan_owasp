"""
Module: referrer_policy_check.py
Checks for the Referrer-Policy header to ensure privacy.
"""
import requests
from rich.console import Console

console = Console()

def check_referrer_policy(url):
    try:
        response = requests.get(url)
        referrer_policy = response.headers.get('Referrer-Policy', None)
        if not referrer_policy:
            console.print("[!] Referrer-Policy header is missing!", style="red")
        else:
            console.print(f"[i] Referrer-Policy: {referrer_policy}")
    except Exception as e:
        console.print(f"[!] Error during Referrer-Policy check: {e}", style="yellow")
