from utils import console

def check_https(url):
    findings = []
    if url.startswith('https://'):
        console.print("[+] HTTPS is enabled", style="green")
    else:
        msg = "HTTPS is NOT enabled"
        console.print(f"[-] {msg}", style="red")
        findings.append(msg)
    return findings
