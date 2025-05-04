"""
Module: htb_ctf_check.py
Looks for HackTheBox-style CTF clues: HTB flags, robots.txt, .git/config, and common admin/dev endpoints.
Summary explanation: This module helps CTF players by automatically searching for HackTheBox-specific flags, exposed sensitive files, and common endpoints that often contain clues or vulnerabilities in CTF challenges. Findings from this module can directly lead to flag discovery or further exploitation paths.
"""
import requests
from rich.console import Console
import re

console = Console()

def check_htb_ctf(url):
    findings = []
    # Check for HTB flag patterns in main page
    try:
        resp = requests.get(url)
        flags = re.findall(r'HTB\{.*?\}', resp.text)
        for flag in flags:
            msg = f"Possible HTB flag found: {flag}"
            console.print(f"[!] {msg}", style="bold red")
            findings.append({"detail": msg, "severity": "High"})
    except Exception as e:
        findings.append({"detail": f"Error fetching main page: {e}", "severity": "Low"})
    # Check for robots.txt
    try:
        robots = requests.get(url.rstrip('/') + '/robots.txt')
        if robots.status_code == 200 and robots.text.strip():
            msg = "robots.txt found and is not empty"
            console.print(f"[!] {msg}", style="yellow")
            findings.append({"detail": msg, "severity": "Medium"})
    except Exception as e:
        findings.append({"detail": f"Error fetching robots.txt: {e}", "severity": "Low"})
    # Check for .git/config
    try:
        git = requests.get(url.rstrip('/') + '/.git/config')
        if git.status_code == 200 and '[core]' in git.text:
            msg = ".git/config found (possible repo leak)"
            console.print(f"[!] {msg}", style="bold red")
            findings.append({"detail": msg, "severity": "High"})
    except Exception as e:
        findings.append({"detail": f"Error fetching .git/config: {e}", "severity": "Low"})
    # Check for common admin/dev endpoints
    for endpoint in ['/admin', '/administrator', '/dev', '/test', '/backup', '/.env']:
        try:
            r = requests.get(url.rstrip('/') + endpoint)
            if r.status_code == 200:
                msg = f"Possible sensitive endpoint found: {endpoint}"
                console.print(f"[!] {msg}", style="yellow")
                findings.append({"detail": msg, "severity": "Medium"})
        except Exception:
            pass
    return findings
