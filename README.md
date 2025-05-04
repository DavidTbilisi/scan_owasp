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
```

## 📦 Install as CLI Tool

You can install and use as a CLI tool:

```bash
pip install .
scan-owasp https://example.com
```

## ⚡ Usage

Scan one or more URLs:

```bash
python scanner.py https://example.com http://test.com
```

Select specific checks (comma-separated):

```bash
python scanner.py https://example.com --checks https,headers,xss
```

Output results to a file (JSON or CSV):

```bash
python scanner.py https://example.com --output results.json
python scanner.py https://example.com --output results.csv
```

## 🔍 Checks Performed
- HTTPS enforcement
- Security headers (CSP, HSTS, X-Frame-Options, X-Content-Type-Options, etc.)
- SQL Injection (basic error-based)
- Directory listing
- Reflected XSS (basic)
- Server version disclosure
- Open redirect
- Cookie security flags
- CORS policy
- Referrer policy
- HSTS preload
- Path traversal (basic)
- Information disclosure (headers, HTML comments)

## 🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

## 📄 License
MIT
