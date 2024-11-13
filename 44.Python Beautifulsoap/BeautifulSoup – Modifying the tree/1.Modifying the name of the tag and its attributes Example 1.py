# importing module
from bs4 import BeautifulSoup

markup = """<p class="para">gfg</p>"""

# parsering string to HTML
soup = BeautifulSoup(markup, 'html.parser')

# extracting a tag
tag = soup.p

print("Before modifing the tag name: ")
print(tag)
print()

# modifing tag name
tag.name = "div"

print("After modifing the tag name: ")
print(tag)
print()
# modifing its class attribute
tag['class'] = "div_class"

# adding new attribute
tag['id'] = "div_id"

print("After modifing and adding attributes: ")
print(tag)
print()

# to delete any attributes
del tag["class"]

print("After deleting class attribute: ")
print(tag)
print()

# modifing the tags conetent
tag.string = "Geeks"

print("After modifing tag string: ")
print(tag)
print()

# using insert function.
tag = soup.div
print("Before inserting: ")
print(tag)
print()

# inserting content
tag.insert(1, " for Geeks")
print("After inserting: ")
print(tag)
print()
