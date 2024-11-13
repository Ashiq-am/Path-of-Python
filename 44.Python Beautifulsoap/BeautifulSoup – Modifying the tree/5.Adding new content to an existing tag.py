# importing module
from bs4 import BeautifulSoup
from bs4 import NavigableString

markup = """<a href="https://www.geeksforgeeks.org/">Geeks for Geeks</a>"""

# parsering string to HTML
soup = BeautifulSoup(markup, 'html.parser')

# extracting a tag
tag = soup.a

# appending content
tag.append("| A Computer Science portal")
print(tag)

# appending content using navigableString contsructor
new_str = NavigableString(" for geeks")
tag.append(new_str)
print(tag)
