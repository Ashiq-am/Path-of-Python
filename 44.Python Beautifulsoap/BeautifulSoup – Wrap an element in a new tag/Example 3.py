# impoting BeautifulSoup Module
from bs4 import BeautifulSoup

markup = '<p>Python 3 </p>'

# parsering string to HTML
soup = BeautifulSoup(markup, 'html.parser')
print(soup)

# wraping around the tag
soup.p.wrap(soup.new_tag("h2"))
print(soup)
