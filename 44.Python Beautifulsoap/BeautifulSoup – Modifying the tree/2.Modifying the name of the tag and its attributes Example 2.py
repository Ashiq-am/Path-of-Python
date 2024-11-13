# importing module
from bs4 import BeautifulSoup

soup = BeautifulSoup("<b>| A Computer Science portal</b>", 'html.parser')

tag = soup.new_tag("p")
tag.string = "Geeks"


# insert before
soup.b.string.insert_before(tag)
print(soup.b)
print()

# insert after
soup.b.p.insert_after(soup.new_string(" for Geeks"))
print(soup.b)
