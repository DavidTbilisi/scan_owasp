"""
Module: dir_listing_check.py
Checks if directory listing is enabled by requesting a common directory and looking for signs of listing.
"""
import requests
from rich.console import Console

console = Console()

def check_dir_listing(url):
    # Try to access a common directory
    if not url.endswith('/'):
        url += '/'
    try:
        response = requests.get(url)
        if 'Index of /' in response.text or '<title>Index of' in response.text:
            console.print("[!] Directory listing appears to be enabled!", style="bold red")
        else:
            console.print("[+] Directory listing does not appear to be enabled.", style="green")
    except Exception as e:
        console.print(f"[!] Error during directory listing check: {e}", style="yellow")
