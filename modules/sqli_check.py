"""
Module: sqli_check.py
Performs a basic SQL Injection check by sending a test payload and looking for SQL error messages in the response.
"""
import requests
from rich.console import Console

console = Console()

def check_sqli(url):
    findings = []
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
            msg = "Possible SQL Injection vulnerability detected!"
            console.print(f"[!] {msg}", style="bold red")
            findings.append(msg)
        else:
            console.print("[+] No obvious SQL Injection vulnerability detected.", style="green")
    except Exception as e:
        msg = f"Error during SQLi check: {e}"
        console.print(f"[!] {msg}", style="yellow")
        findings.append(msg)
    return findings
