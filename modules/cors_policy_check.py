"""
Module: cors_policy_check.py
Checks the CORS policy by inspecting the Access-Control-Allow-Origin header.
"""
import requests
from rich.console import Console

console = Console()

def check_cors_policy(url):
    try:
        response = requests.get(url)
        cors = response.headers.get('Access-Control-Allow-Origin', None)
        if cors == '*':
            console.print("[!] CORS policy is too permissive: Access-Control-Allow-Origin: *", style="red")
        elif cors:
            console.print(f"[i] CORS policy: Access-Control-Allow-Origin: {cors}")
        else:
            console.print("[i] No CORS policy set.")
    except Exception as e:
        console.print(f"[!] Error during CORS policy check: {e}", style="yellow")
