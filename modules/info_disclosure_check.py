"""
Module: info_disclosure_check.py
Looks for sensitive information in headers, error messages, or comments in the HTML.
"""
import requests
from utils import console, safe_get
import re

def check_info_disclosure(url):
    findings = []
    response = safe_get(url, 'information disclosure', findings)
    if not response:
        return findings
    # Check for common sensitive headers
    for header in ['X-AspNet-Version', 'X-Powered-By', 'Server']:
        if header in response.headers:
            msg = f"Information disclosure in header: {header}: {response.headers[header]}"
            console.print(f"[!] {msg}", style="red")
            findings.append(msg)
    # Check for sensitive info in HTML comments
    comments = re.findall(r'<!--(.*?)-->', response.text, re.DOTALL)
    for comment in comments:
        if any(word in comment.lower() for word in ['password', 'secret', 'key', 'token']):
            msg = f"Sensitive info in HTML comment: {comment.strip()}"
            console.print(f"[!] {msg}", style="red")
            findings.append(msg)
    return findings
