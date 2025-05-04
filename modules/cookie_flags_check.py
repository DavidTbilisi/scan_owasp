"""
Module: cookie_flags_check.py
Checks if cookies set by the server have Secure and HttpOnly flags.
"""
import requests
from rich.console import Console

console = Console()

def check_cookie_flags(url):
    try:
        response = requests.get(url)
        cookies = response.headers.get('Set-Cookie', '')
        if not cookies:
            console.print("[i] No cookies set by the server.")
            return
        for cookie in cookies.split(','):
            cookie = cookie.strip()
            if 'secure' not in cookie.lower():
                console.print(f"[!] Cookie missing Secure flag: {cookie}", style="red")
            if 'httponly' not in cookie.lower():
                console.print(f"[!] Cookie missing HttpOnly flag: {cookie}", style="red")
            if 'secure' in cookie.lower() and 'httponly' in cookie.lower():
                console.print(f"[+] Cookie has Secure and HttpOnly flags: {cookie}", style="green")
    except Exception as e:
        console.print(f"[!] Error during cookie flags check: {e}", style="yellow")
