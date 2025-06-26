"""
Zomato Scraper Package.

A Python package for scraping restaurant data and menus from Zomato.
Uses IP-based geolocation to automatically detect user location and
extract comprehensive restaurant information.

Author: Abhay Shinde
License: MIT
"""

from .zomato_scrapper import zomato

__version__ = "1.0.0"
__author__ = "Abhay Shinde"
__license__ = "MIT"

__all__ = ["zomato"] 