"""
Module: server_version_check.py
Checks for outdated or potentially vulnerable server software by inspecting the Server and X-Powered-By headers.
"""
import requests
from rich.console import Console

console = Console()

def check_server_version(url):
    findings = []
    try:
        response = requests.get(url)
        server = response.headers.get('Server', 'Unknown')
        powered_by = response.headers.get('X-Powered-By', 'Unknown')
        console.print(f"[i] Server header: {server}")
        console.print(f"[i] X-Powered-By header: {powered_by}")
        # Example: flag if version is old (expand as needed)
        if server != 'Unknown':
            findings.append(f"Server header: {server}")
        if powered_by != 'Unknown':
            findings.append(f"X-Powered-By header: {powered_by}")
    except Exception as e:
        msg = f"Error during server version check: {e}"
        console.print(f"[!] {msg}", style="yellow")
        findings.append(msg)
    return findings
