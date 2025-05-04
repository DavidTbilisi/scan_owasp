from rich.console import Console

console = Console()

def check_https(url):
    if url.startswith('https://'):
        console.print("[+] HTTPS is enabled", style="green")
    else:
        console.print("[-] HTTPS is NOT enabled", style="red")
