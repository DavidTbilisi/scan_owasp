"""
Module: cors_policy_check.py
Checks the CORS policy by inspecting the Access-Control-Allow-Origin header.
"""
import requests
from utils import console, safe_get

def check_cors_policy(url):
    findings = []
    response = safe_get(url, 'CORS policy', findings)
    if not response:
        return findings
    cors = response.headers.get('Access-Control-Allow-Origin', None)
    if cors == '*':
        msg = "CORS policy is too permissive: Access-Control-Allow-Origin: *"
        console.print(f"[!] {msg}", style="red")
        findings.append(msg)
    elif cors:
        console.print(f"[i] CORS policy: Access-Control-Allow-Origin: {cors}")
    else:
        msg = "No CORS policy set."
        console.print(f"[i] {msg}")
        findings.append(msg)
    return findings
