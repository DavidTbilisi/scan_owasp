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
from modules.server_version_check import check_server_version
from modules.open_redirect_check import check_open_redirect
from modules.cookie_flags_check import check_cookie_flags
from modules.cors_policy_check import check_cors_policy
from modules.referrer_policy_check import check_referrer_policy
from modules.hsts_preload_check import check_hsts_preload
from modules.path_traversal_check import check_path_traversal
from modules.info_disclosure_check import check_info_disclosure

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
    check_server_version(url)
    check_open_redirect(url)
    check_cookie_flags(url)
    check_cors_policy(url)
    check_referrer_policy(url)
    check_hsts_preload(url)
    check_path_traversal(url)
    check_info_disclosure(url)

if __name__ == "__main__":
    main()
