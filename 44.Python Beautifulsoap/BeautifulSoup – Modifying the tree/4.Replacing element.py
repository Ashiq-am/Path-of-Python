# impoting BeautifulSoup Module
from bs4 import BeautifulSoup

markup = '<a href="http://gfg.com/">Geeks for Geeks <i>gfg.com</i></a>'

# parsering string to HTML
soup = BeautifulSoup(markup, 'html.parser')

# tag to be replaced
old_tag = soup.a

# new tag
new_tag = soup.new_tag("p")

# input string
new_tag.string = "gfg.in"

'''replacing tag page_element.replace_with("string")
removes a tag or string from the tree, and replaces
it with the tag or string of your choice.'''

old_tag.i.replace_with(new_tag)

print(old_tag)
