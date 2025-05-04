from rich.console import Console
import requests

console = Console()

def check_headers(url):
    try:
        response = requests.get(url)
        headers = response.headers
        required_headers = [
            "Content-Security-Policy",
            "Strict-Transport-Security",
            "X-Content-Type-Options",
            "X-Frame-Options"
        ]
        for header in required_headers:
            if header not in headers:
                console.print(f"[-] Missing security header: {header}", style="red")
            else:
                console.print(f"[+] Found security header: {header}", style="green")
    except Exception as e:
        console.print(f"[!] Error fetching headers: {e}", style="bold yellow")
