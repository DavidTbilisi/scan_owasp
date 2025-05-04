"""
Module: info_disclosure_check.py
Looks for sensitive information in headers, error messages, or comments in the HTML.
"""
import requests
from rich.console import Console
import re

console = Console()

def check_info_disclosure(url):
    findings = []
    try:
        response = requests.get(url)
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
    except Exception as e:
        msg = f"Error during information disclosure check: {e}"
        console.print(f"[!] {msg}", style="yellow")
        findings.append(msg)
    return findings
