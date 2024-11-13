# Python program to get data inside
# a button tag using BeautifulSoup

# Import the libraries BeautifulSoup
# and os
from bs4 import BeautifulSoup as bs
import os

# Remove the last segment of the path
base = os.path.dirname(os.path.abspath(__file__))

# Open the HTML in which you want to make
# changes
html = open(os.path.join(base, 'run.html'))

# Parse HTML file in Beautiful Soup
soup = bs(html, 'html.parser')

# Finding the location of button
btn = soup.find("button", {"id": "enjoy"})

# Obtaining the text stored inside button tag
btn_text = btn.text

# Obtaining the onclick link of button tag
btn_onclick = btn['onclick']

# Printing the values
print(btn_text)
print(btn_onclick)
