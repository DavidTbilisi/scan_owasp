import requests
from bs4 import BeautifulSoup
import sys

def check_https(url):
    if url.startswith('https://'):
        print("[+] HTTPS is enabled")
    else:
        print("[-] HTTPS is NOT enabled")

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
                print(f"[-] Missing security header: {header}")
            else:
                print(f"[+] Found security header: {header}")
    except Exception as e:
        print(f"Error fetching headers: {e}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python scanner.py <URL>")
        sys.exit(1)

    url = sys.argv[1]
    check_https(url)
    check_headers(url)

if __name__ == "__main__":
    main()
