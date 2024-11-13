# Python program to find a HTML tag
# that contains certain text Using BeautifulSoup

# Importing library
from bs4 import BeautifulSoup
import re

# Opening and reading the html file
file = open("gfg.html", "r")
contents = file.read()

soup = BeautifulSoup(contents, 'html.parser')

# Finding a pattern(certain text)
pattern = 'Geeks For Geeks'

# Anchor tag
text1 = soup.find_all('a', text = pattern)
print(text1)

# Span tag
text2 = soup.find_all('span', text = pattern)
print(text2)

# Finding a pattern(certain text)
pattern2 = 'Python Program'

# Heading tag
text3 = soup.find_all('h1', text = pattern2)
print(text3)

# List tag
text4 = soup.find_all('li', text = pattern2)
print(text4)

# Finding a pattern(certain text)
pattern3 = 'GFG Website'

# Table(row) tag
text5 = soup.find_all('tr', text = pattern3)
print(text5)
