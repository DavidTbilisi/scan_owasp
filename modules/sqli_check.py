"""
Module: sqli_check.py
Performs a basic SQL Injection check by sending a test payload and looking for SQL error messages in the response.
"""
import requests
from rich.console import Console

console = Console()

def check_sqli(url):
    # Add a simple SQL injection payload to the URL
    test_url = url + ("?id=1' OR '1'='1" if '?' not in url else "' OR '1'='1")
    try:
        response = requests.get(test_url)
        errors = [
            'you have an error in your sql syntax',
            'warning: mysql',
            'unclosed quotation mark after the character string',
            'quoted string not properly terminated',
            'sql syntax',
        ]
        if any(error in response.text.lower() for error in errors):
            console.print("[!] Possible SQL Injection vulnerability detected!", style="bold red")
        else:
            console.print("[+] No obvious SQL Injection vulnerability detected.", style="green")
    except Exception as e:
        console.print(f"[!] Error during SQLi check: {e}", style="yellow")
