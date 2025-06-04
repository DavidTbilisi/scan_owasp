"""
Module: path_traversal_check.py
Performs a basic path traversal check by injecting ../ into parameters and looking for error messages or directory listings.
"""
import requests
from utils import console, safe_get
from urllib.parse import urljoin

def check_path_traversal(url):
    findings = []
    payload = '../etc/passwd'
    test_url = urljoin(url, f'?file={payload}')
    response = safe_get(test_url, 'path traversal', findings)
    if not response:
        return findings
    if 'root:x:' in response.text or 'No such file or directory' in response.text or 'not found' in response.text:
        msg = "Possible path traversal vulnerability detected!"
        console.print(f"[!] {msg}", style="bold red")
        findings.append(msg)
    else:
        console.print("[+] No obvious path traversal vulnerability detected.", style="green")
    return findings
