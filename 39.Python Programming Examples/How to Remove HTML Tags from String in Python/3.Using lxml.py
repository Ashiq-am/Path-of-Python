from lxml.html import fromstring

# Sample string with HTML tags
s1 = "<h1>Welcome to Python Programming</h1>"

# Removing HTML tags using lxml
tree = fromstring(s1)
s2 = tree.text_content()
print(s2)