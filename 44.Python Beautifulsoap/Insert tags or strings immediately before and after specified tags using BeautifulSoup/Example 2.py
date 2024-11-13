# import module
from bs4 import BeautifulSoup

# assign URL
s = BeautifulSoup("<b>www.geeksforgeeks.com</b>",
				"lxml")

print("Original Markup:")
print(s.b)

# insert tag
tag = s.new_tag("k")
tag.string = "Python"

print("\nNew Markup, before inserting the text:")
s.b.string.insert_after(tag)
print(s.b)
