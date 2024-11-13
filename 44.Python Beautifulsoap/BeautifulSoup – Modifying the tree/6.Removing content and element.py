# importing module
from bs4 import BeautifulSoup

markup = '<a href="https://www.geeksforgeeks.org/">Geeks for Geeks <i>| A Computer Science portal</i></a>'

# parsering string to HTML
soup = BeautifulSoup(markup, 'html.parser')

tag = soup.a
print(tag)
print()

# clearing its all content
tag.clear()
print(tag)
print()

# extracting i tag
# parsering string to HTML
soup2 = BeautifulSoup(markup, 'html.parser')

a_tag = soup2.a

print(a_tag)
print()
i_tag = soup2.i.extract()

print(a_tag)
print()

# decomposing i tag
# parsering string to HTML
soup2 = BeautifulSoup(markup, 'html.parser')

a_tag = soup2.a

print(a_tag)
print()
i_tag = soup2.i.decompose()

print(a_tag)
