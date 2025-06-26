#!/usr/bin/env python3
"""
Setup script for Zomato Scraper

This script allows the project to be installed via pip and provides
proper metadata for PyPI distribution.
"""

from setuptools import setup, find_packages
import os

# Read the README file
def read_readme():
    """Read the README.md file."""
    readme_path = os.path.join(os.path.dirname(__file__), 'README.md')
    if os.path.exists(readme_path):
        with open(readme_path, 'r', encoding='utf-8') as f:
            return f.read()
    return "A Python scraper for extracting restaurant data and menus from Zomato."

# Read requirements
def read_requirements():
    """Read the requirements.txt file."""
    requirements_path = os.path.join(os.path.dirname(__file__), 'requirements.txt')
    if os.path.exists(requirements_path):
        with open(requirements_path, 'r', encoding='utf-8') as f:
            return [line.strip() for line in f if line.strip() and not line.startswith('#')]
    return ['requests>=2.32.0']

setup(
    name="zomato-scraper",
    version="1.0.0",
    author="Abhay Shinde",
    author_email="abhayshinde444@gmail.com",
    description="A high-performance Python scraper for extracting restaurant data and menus from Zomato",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/224Abhay/zomato-scraper",
    project_urls={
        "Bug Tracker": "https://github.com/224Abhay/zomato-scraper/issues",
        "Documentation": "https://github.com/224Abhay/zomato-scraper#readme",
        "Source Code": "https://github.com/224Abhay/zomato-scraper",
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Internet :: WWW/HTTP :: Browsers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
    ],
    keywords="zomato, scraper, restaurant, menu, food, delivery, python, web-scraping",
    packages=find_packages(),
    python_requires=">=3.7",
    install_requires=read_requirements(),
    extras_require={
        "dev": [
            "pytest>=6.0",
            "pytest-cov>=2.0",
            "black>=21.0",
            "flake8>=3.8",
            "mypy>=0.800",
        ],
    },
    entry_points={
        "console_scripts": [
            "zomato-scraper=main:main",
        ],
    },
    include_package_data=True,
    zip_safe=False,
    platforms=["any"],
    license="MIT",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Internet :: WWW/HTTP :: Browsers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
    ],
) 