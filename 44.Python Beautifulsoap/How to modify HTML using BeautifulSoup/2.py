# Python program to modify HTML
# with the help of Beautiful Soup

# Import the libraries
from bs4 import BeautifulSoup as bs
import os
import re

# Remove the last segment of the path
base = os.path.dirname(os.path.abspath(__file__))

# Open the HTML in which you want to make changes
html = open(os.path.join(base, 'gfg.html'))

# Parse HTML file in Beautiful Soup
soup = bs(html, 'html.parser')

# Give location where text is
# stored which you wish to alter
old_text = soup.find("p", {"id": "para"})

# Replace the already stored text with
# the new text which you wish to assign
new_text = old_text.find(text=re.compile('Geeks For Geeks')).replace_with('Vinayak Rai')

# Alter HTML file to see the changes done
with open("gfg.html", "wb") as f_output:
    f_output.write(soup.prettify("utf-8"))
