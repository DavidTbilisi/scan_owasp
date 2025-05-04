"""
Module: info_disclosure_check.py
Looks for sensitive information in headers, error messages, or comments in the HTML.
"""
import requests
from rich.console import Console
import re

console = Console()

def check_info_disclosure(url):
    try:
        response = requests.get(url)
        # Check for common sensitive headers
        for header in ['X-AspNet-Version', 'X-Powered-By', 'Server']:
            if header in response.headers:
                console.print(f"[!] Information disclosure in header: {header}: {response.headers[header]}", style="red")
        # Check for sensitive info in HTML comments
        comments = re.findall(r'<!--(.*?)-->', response.text, re.DOTALL)
        for comment in comments:
            if any(word in comment.lower() for word in ['password', 'secret', 'key', 'token']):
                console.print(f"[!] Sensitive info in HTML comment: {comment.strip()}", style="red")
    except Exception as e:
        console.print(f"[!] Error during information disclosure check: {e}", style="yellow")
