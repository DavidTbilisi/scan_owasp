"""
Module: server_version_check.py
Checks for outdated or potentially vulnerable server software by inspecting the Server and X-Powered-By headers.
"""
import requests
from rich.console import Console

console = Console()

def check_server_version(url):
    try:
        response = requests.get(url)
        server = response.headers.get('Server', 'Unknown')
        powered_by = response.headers.get('X-Powered-By', 'Unknown')
        console.print(f"[i] Server header: {server}")
        console.print(f"[i] X-Powered-By header: {powered_by}")
        # You can expand this with a list of known vulnerable versions
    except Exception as e:
        console.print(f"[!] Error during server version check: {e}", style="yellow")
