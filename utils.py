from rich.console import Console
import requests

console = Console()

def safe_request(method, url, check_name, findings, **kwargs):
    """Wrapper for requests.request with standardized error handling."""
    try:
        return requests.request(method, url, **kwargs)
    except Exception as e:
        msg = f"Error during {check_name} check: {e}"
        console.print(f"[!] {msg}", style="yellow")
        findings.append(msg)
        return None

def safe_get(url, check_name, findings, **kwargs):
    """Shortcut for GET requests."""
    return safe_request("GET", url, check_name, findings, **kwargs)
