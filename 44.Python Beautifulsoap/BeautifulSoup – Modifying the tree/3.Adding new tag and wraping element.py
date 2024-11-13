# importing module
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

# unwrapin the i tag

soup.p.i.unwrap()

print(soup)

old_tag = soup.div

# new tag
new_tag = soup.new_tag('div')
new_tag.string = "| A Computer Science portal for geeks"

# adding new tag
old_tag.append(new_tag)

print(soup)
