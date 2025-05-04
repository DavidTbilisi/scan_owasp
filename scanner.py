import requests
from bs4 import BeautifulSoup
import click
from rich.console import Console

console = Console()

import click
from modules.https_check import check_https
from modules.headers_check import check_headers
from modules.sqli_check import check_sqli
from modules.dir_listing_check import check_dir_listing
from modules.xss_check import check_xss

"""
scanner.py
Main entry point for the modular OWASP Top 10 scanner.
Each check is implemented in its own module for maintainability and extensibility.
Add or remove checks by importing the relevant modules and calling their functions below.
"""

@click.command()
@click.argument('url')
def main(url):
    """
    Simple OWASP scanner for a given URL.
    Each check prints its own results to the console.
    """
    check_https(url)
    check_headers(url)
    check_sqli(url)
    check_dir_listing(url)
    check_xss(url)

if __name__ == "__main__":
    main()
