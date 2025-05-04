"""
Module: thm_ctf_check.py
Looks for TryHackMe-style CTF clues: THM/FLAG patterns, exposed backup/config files, and common CTF endpoints.
Summary explanation: This module is designed for CTF players on TryHackMe. It searches for TryHackMe-specific flags, exposed backup/config files, and endpoints that are commonly used to hide flags or clues in CTF challenges. Findings from this module can help quickly identify key targets or vulnerabilities during a CTF.
"""
import requests
from rich.console import Console
import re

console = Console()

def check_thm_ctf(url):
    findings = []
    # Check for THM/FLAG patterns in main page
    try:
        resp = requests.get(url)
        flags = re.findall(r'(THM\{.*?\}|FLAG\{.*?\})', resp.text)
        for flag in flags:
            msg = f"Possible THM/FLAG found: {flag}"
            console.print(f"[!] {msg}", style="bold red")
            findings.append({"detail": msg, "severity": "High"})
    except Exception as e:
        findings.append({"detail": f"Error fetching main page: {e}", "severity": "Low"})
    # Check for exposed backup/config files
    for ext in ['.bak', '.old', '.zip', '.tar.gz', '.env', '.config']:
        try:
            r = requests.get(url.rstrip('/') + '/index.php' + ext)
            if r.status_code == 200 and len(r.content) > 0:
                msg = f"Possible backup/config file found: /index.php{ext}"
                console.print(f"[!] {msg}", style="yellow")
                findings.append({"detail": msg, "severity": "Medium"})
        except Exception:
            pass
    # Check for /flag, /secret, /hidden endpoints
    for endpoint in ['/flag', '/secret', '/hidden', '/.env']:
        try:
            r = requests.get(url.rstrip('/') + endpoint)
            if r.status_code == 200:
                msg = f"Possible CTF endpoint found: {endpoint}"
                console.print(f"[!] {msg}", style="yellow")
                findings.append({"detail": msg, "severity": "Medium"})
        except Exception:
            pass
    return findings
