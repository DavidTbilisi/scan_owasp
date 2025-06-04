"""
Module: referrer_policy_check.py
Checks for the Referrer-Policy header to ensure privacy.
"""
import requests
from utils import console, safe_get

def check_referrer_policy(url):
    findings = []
    response = safe_get(url, 'Referrer-Policy', findings)
    if not response:
        return findings
    referrer_policy = response.headers.get('Referrer-Policy', None)
    if not referrer_policy:
        msg = "Referrer-Policy header is missing!"
        console.print(f"[!] {msg}", style="red")
        findings.append(msg)
    else:
        console.print(f"[i] Referrer-Policy: {referrer_policy}")
    return findings
