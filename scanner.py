import requests
from bs4 import BeautifulSoup
import click
from utils import console
import json
from typing import List

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
from modules.htb_ctf_check import check_htb_ctf
from modules.thm_ctf_check import check_thm_ctf
from modules.idor_check import check_idor
from modules.verb_tampering_check import check_verb_tampering

# Registry of all available checks
ALL_CHECKS = {
    'https': check_https,
    'headers': check_headers,
    'sqli': check_sqli,
    'dir_listing': check_dir_listing,
    'xss': check_xss,
    'server_version': check_server_version,
    'open_redirect': check_open_redirect,
    'cookie_flags': check_cookie_flags,
    'cors_policy': check_cors_policy,
    'referrer_policy': check_referrer_policy,
    'hsts_preload': check_hsts_preload,
    'path_traversal': check_path_traversal,
    'info_disclosure': check_info_disclosure,
    'htb_ctf': check_htb_ctf,
    'thm_ctf': check_thm_ctf,
    'idor': check_idor,
    'verb_tampering': check_verb_tampering,
}

"""
scanner.py
Main entry point for the modular OWASP Top 10 scanner.
Each check is implemented in its own module for maintainability and extensibility.
Add or remove checks by importing the relevant modules and calling their functions below.
"""

@click.command()
@click.argument('urls', nargs=-1)
@click.option('--checks', default='all', help='Comma-separated list of checks to run (e.g. "https,headers,xss,idor,verb_tampering"). Use "all" to run every check. Run with --list-checks to see available checks. (default: all)')
@click.option('--list-checks', is_flag=True, default=False, help='List all available checks and exit.')
@click.option('--output', default=None, help='Output file (JSON or CSV)')
def main(urls: List[str], checks, output, list_checks):
    """
    Modular OWASP scanner for one or more URLs.
    """
    if list_checks:
        console.print("[bold green]Available checks:")
        for check in ALL_CHECKS:
            console.print(f"- {check}")
        return
    if not urls:
        console.print('[bold red]No URLs provided![/bold red]')
        console.print('[yellow]Usage: python scanner.py <url1> [url2 ...] --checks <check1,check2,...>')
        console.print('[yellow]Use --list-checks to see all available checks.')
        return
    if checks == '':
        console.print('[bold red]Error: Option --checks requires an argument.[/bold red]')
        console.print('[yellow]Example: --checks https,headers,xss')
        console.print('[yellow]Use --list-checks to see all available checks.')
        return
    selected_checks = list(ALL_CHECKS.keys()) if checks == 'all' else [c.strip() for c in checks.split(',') if c.strip() in ALL_CHECKS]
    results = []
    for url in urls:
        console.rule(f"[bold blue]Scanning: {url}")
        url_result = {'url': url, 'findings': []}
        for check_name in selected_checks:
            try:
                findings = ALL_CHECKS[check_name](url)
                if findings:
                    for finding in findings:
                        # If finding is a dict with detail/severity, use it; else, wrap as dict
                        if isinstance(finding, dict):
                            url_result['findings'].append({'check': check_name, **finding})
                        else:
                            url_result['findings'].append({'check': check_name, 'detail': finding, 'severity': 'Info'})
            except Exception as e:
                console.print(f"[!] Error in {check_name}: {e}", style="yellow")
        results.append(url_result)
    # Summary
    console.rule("[bold green]Scan Summary")
    for res in results:
        console.print(f"[bold]{res['url']}[/bold]: {len(res['findings'])} findings")
        for finding in res['findings']:
            sev = finding.get('severity', 'Info')
            sev_color = {'High': 'bold red', 'Medium': 'yellow', 'Low': 'blue', 'Info': 'white'}.get(sev, 'white')
            console.print(f"  [bold]{sev}[/bold] [red]- {finding['check']}: {finding['detail']}", style=sev_color)
    # Output to file
    if output:
        if output.endswith('.json'):
            with open(output, 'w', encoding='utf-8') as f:
                json.dump(results, f, indent=2)
            console.print(f"[green]Results saved to {output}")
        elif output.endswith('.csv'):
            import csv
            with open(output, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(['url', 'check', 'finding'])
                for res in results:
                    for finding in res['findings']:
                        writer.writerow([res['url'], finding['check'], finding['detail']])
            console.print(f"[green]Results saved to {output}")
        else:
            console.print("[yellow]Unknown output format. Use .json or .csv")

if __name__ == "__main__":
    main()
