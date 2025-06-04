"""
Module: thm_ctf_check.py
Looks for TryHackMe-style CTF clues: THM/FLAG patterns, exposed backup/config files, and common CTF endpoints.
Summary explanation: This module is designed for CTF players on TryHackMe. It searches for TryHackMe-specific flags, exposed backup/config files, and endpoints that are commonly used to hide flags or clues in CTF challenges. Findings from this module can help quickly identify key targets or vulnerabilities during a CTF.
"""
import requests
from utils import console, safe_get
import re

def check_thm_ctf(url):
    findings = []
    # Check for THM/FLAG patterns in main page
    resp = safe_get(url, 'THM main', findings)
    if resp:
        flags = re.findall(r'(THM\{.*?\}|FLAG\{.*?\})', resp.text)
        for flag in flags:
            msg = f"Possible THM/FLAG found: {flag}"
            console.print(f"[!] {msg}", style="bold red")
            findings.append({"detail": msg, "severity": "High"})
    # Check for exposed backup/config files
    for ext in ['.bak', '.old', '.zip', '.tar.gz', '.env', '.config']:
        r = safe_get(url.rstrip('/') + '/index.php' + ext, 'THM backup', findings)
        if r and r.status_code == 200 and len(r.content) > 0:
            msg = f"Possible backup/config file found: /index.php{ext}"
            console.print(f"[!] {msg}", style="yellow")
            findings.append({"detail": msg, "severity": "Medium"})
    # Check for /flag, /secret, /hidden endpoints
    for endpoint in ['/flag', '/secret', '/hidden', '/.env']:
        r = safe_get(url.rstrip('/') + endpoint, 'THM endpoint', findings)
        if r and r.status_code == 200:
            msg = f"Possible CTF endpoint found: {endpoint}"
            console.print(f"[!] {msg}", style="yellow")
            findings.append({"detail": msg, "severity": "Medium"})
    return findings
