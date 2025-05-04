"""
Module: cookie_flags_check.py
Checks if cookies set by the server have Secure and HttpOnly flags.
"""
import requests
from rich.console import Console

console = Console()

def check_cookie_flags(url):
    findings = []
    try:
        response = requests.get(url)
        cookies = response.headers.get('Set-Cookie', '')
        if not cookies:
            console.print("[i] No cookies set by the server.")
            return findings
        for cookie in cookies.split(','):
            cookie = cookie.strip()
            if 'secure' not in cookie.lower():
                msg = f"Cookie missing Secure flag: {cookie}"
                console.print(f"[!] {msg}", style="red")
                findings.append(msg)
            if 'httponly' not in cookie.lower():
                msg = f"Cookie missing HttpOnly flag: {cookie}"
                console.print(f"[!] {msg}", style="red")
                findings.append(msg)
            if 'secure' in cookie.lower() and 'httponly' in cookie.lower():
                console.print(f"[+] Cookie has Secure and HttpOnly flags: {cookie}", style="green")
    except Exception as e:
        msg = f"Error during cookie flags check: {e}"
        console.print(f"[!] {msg}", style="yellow")
        findings.append(msg)
    return findings
