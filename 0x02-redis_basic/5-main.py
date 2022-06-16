#!/usr/bin/env python3
"""Implementing an expiring web cache and tracker"""

from web import get_page

URL = "http://slowwly.robertomurray.co.uk/delay/5000/url/https://web.ics.purdue.edu/~gchopra/class/public/pages/webdesign/05_simple.html"

print("first get_page")
print(get_page(URL))
print("\n\n\n")
print("second get_page")
print(get_page(URL))
