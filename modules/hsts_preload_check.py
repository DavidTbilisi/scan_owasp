"""
Module: hsts_preload_check.py
Checks if Strict-Transport-Security is set with preload, max-age, and includeSubDomains.
"""
import requests
from utils import console, safe_get

def check_hsts_preload(url):
    findings = []
    response = safe_get(url, 'HSTS preload', findings)
    if not response:
        return findings
    hsts = response.headers.get('Strict-Transport-Security', None)
    if not hsts:
        msg = "Strict-Transport-Security header is missing!"
        console.print(f"[!] {msg}", style="red")
        findings.append(msg)
        return findings
    if 'preload' in hsts and 'max-age=' in hsts and 'includesubdomains' in hsts.lower():
        console.print(f"[+] HSTS is properly configured for preload: {hsts}", style="green")
    else:
        msg = f"HSTS header is present but not fully configured for preload: {hsts}"
        console.print(f"[!] {msg}", style="yellow")
        findings.append(msg)
    return findings
