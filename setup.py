from setuptools import setup, find_packages

setup(
    name='scan_owasp',
    version='1.0.0',
    description='Modular OWASP Top 10 Web Scanner',
    author='David Chincharashvili',
    packages=find_packages(),
    py_modules=['scanner'],
    install_requires=[
        'requests',
        'rich',
        'click',
        'beautifulsoup4'
    ],
    entry_points={
        'console_scripts': [
            'scan-owasp=scanner:main',
        ],
    },
    python_requires='>=3.8',
)
