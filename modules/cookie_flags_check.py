"""
Module: cookie_flags_check.py
Checks if cookies set by the server have Secure and HttpOnly flags.
"""
import requests
from utils import console, safe_get

def check_cookie_flags(url):
    findings = []
    response = safe_get(url, 'cookie flags', findings)
    if not response:
        return findings
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
    return findings
