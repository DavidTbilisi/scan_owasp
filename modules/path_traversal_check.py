"""
Module: path_traversal_check.py
Performs a basic path traversal check by injecting ../ into parameters and looking for error messages or directory listings.
"""
import requests
from rich.console import Console
from urllib.parse import urljoin

console = Console()

def check_path_traversal(url):
    findings = []
    payload = '../etc/passwd'
    test_url = urljoin(url, f'?file={payload}')
    try:
        response = requests.get(test_url)
        if 'root:x:' in response.text or 'No such file or directory' in response.text or 'not found' in response.text:
            msg = "Possible path traversal vulnerability detected!"
            console.print(f"[!] {msg}", style="bold red")
            findings.append(msg)
        else:
            console.print("[+] No obvious path traversal vulnerability detected.", style="green")
    except Exception as e:
        msg = f"Error during path traversal check: {e}"
        console.print(f"[!] {msg}", style="yellow")
        findings.append(msg)
    return findings
