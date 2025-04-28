# 🛡️ Mini-OWASP Scanner

A lightweight, open-source Python tool that performs basic web application security checks based on the OWASP Top 10 vulnerabilities.

## 🚀 Features
- Checks if HTTPS is enforced
- Detects missing security headers:
  - Content-Security-Policy (CSP)
  - X-Frame-Options
  - X-Content-Type-Options
  - Strict-Transport-Security (HSTS)
- Looks for potential Open Redirect vulnerabilities
- Scans for basic XSS patterns in form inputs

## 🛠️ Tech Stack
- Python 3
- Requests
- BeautifulSoup4

## 📦 Installation

```bash
git clone https://github.com/davidtbilisi/scan_owasp.git
cd scan_owasp
pip install -r requirements.txt
