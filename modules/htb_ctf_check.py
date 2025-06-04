"""
Module: htb_ctf_check.py
Looks for HackTheBox-style CTF clues: HTB flags, robots.txt, .git/config, and common admin/dev endpoints.
Summary explanation: This module helps CTF players by automatically searching for HackTheBox-specific flags, exposed sensitive files, and common endpoints that often contain clues or vulnerabilities in CTF challenges. Findings from this module can directly lead to flag discovery or further exploitation paths.
"""
import requests
from utils import console, safe_get
import re

def check_htb_ctf(url):
    findings = []
    # Check for HTB flag patterns in main page
    resp = safe_get(url, 'HTB main', findings)
    if resp:
        flags = re.findall(r'HTB\{.*?\}', resp.text)
        for flag in flags:
            msg = f"Possible HTB flag found: {flag}"
            console.print(f"[!] {msg}", style="bold red")
            findings.append({"detail": msg, "severity": "High"})
    # Check for robots.txt
    robots = safe_get(url.rstrip('/') + '/robots.txt', 'HTB robots', findings)
    if robots and robots.status_code == 200 and robots.text.strip():
        msg = "robots.txt found and is not empty"
        console.print(f"[!] {msg}", style="yellow")
        findings.append({"detail": msg, "severity": "Medium"})
    # Check for .git/config
    git = safe_get(url.rstrip('/') + '/.git/config', 'HTB git', findings)
    if git and git.status_code == 200 and '[core]' in git.text:
        msg = ".git/config found (possible repo leak)"
        console.print(f"[!] {msg}", style="bold red")
        findings.append({"detail": msg, "severity": "High"})
    # Check for common admin/dev endpoints
    for endpoint in ['/admin', '/administrator', '/dev', '/test', '/backup', '/.env']:
        r = safe_get(url.rstrip('/') + endpoint, 'HTB endpoint', findings)
        if r and r.status_code == 200:
            msg = f"Possible sensitive endpoint found: {endpoint}"
            console.print(f"[!] {msg}", style="yellow")
            findings.append({"detail": msg, "severity": "Medium"})
    return findings
