# impoting BeautifulSoup Module
from bs4 import BeautifulSoup

markup = '<p>Geeks for Geeks</p>'

# parsering string to HTML
soup = BeautifulSoup(markup, 'html.parser')
print(soup)

# wraping around the string
soup.p.string.wrap(soup.new_tag("i"))
print(soup)

# wraping around the tag
soup.p.wrap(soup.new_tag("div"))
print(soup)
