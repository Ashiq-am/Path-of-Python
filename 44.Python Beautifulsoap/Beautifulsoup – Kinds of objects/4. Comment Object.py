# Import Beautiful Soup
from bs4 import BeautifulSoup

# Create the document
markup = "<b><!-- COMMENT --></b>"

# Initialize the object with the document
soup = BeautifulSoup(markup, "html.parser")

# Get the whole comment inside b tag
comment = soup.b.string

# Print the type of the comment
print(type(comment))
