from rich.console import Console
import requests

console = Console()

def check_headers(url):
    findings = []
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
                msg = f"Missing security header: {header}"
                console.print(f"[-] {msg}", style="red")
                # Assign severity based on header importance
                severity = "High" if header in ["Content-Security-Policy", "Strict-Transport-Security"] else "Medium"
                findings.append({"detail": msg, "severity": severity})
            else:
                console.print(f"[+] Found security header: {header}", style="green")
    except Exception as e:
        msg = f"Error fetching headers: {e}"
        console.print(f"[!] {msg}", style="bold yellow")
        findings.append({"detail": msg, "severity": "Low"})
    return findings
