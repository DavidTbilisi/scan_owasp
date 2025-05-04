"""
Module: open_redirect_check.py
Checks for open redirect vulnerabilities by testing common redirect parameters.
"""
import requests
from rich.console import Console
from urllib.parse import urlparse, urljoin

console = Console()

def check_open_redirect(url):
    findings = []
    # List of common redirect parameters
    params = ['next', 'url', 'redirect', 'redir', 'dest', 'destination']
    payload = 'https://evil.com'
    for param in params:
        test_url = urljoin(url, f'?{param}={payload}')
        try:
            response = requests.get(test_url, allow_redirects=False)
            if response.status_code in [301, 302, 303, 307, 308]:
                location = response.headers.get('Location', '')
                if payload in location:
                    msg = f"Possible open redirect via '{param}' parameter!"
                    console.print(f"[!] {msg}", style="bold red")
                    findings.append(msg)
        except Exception as e:
            msg = f"Error during open redirect check: {e}"
            console.print(f"[!] {msg}", style="yellow")
            findings.append(msg)
    return findings
