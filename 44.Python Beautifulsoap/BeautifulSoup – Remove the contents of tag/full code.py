# Importing libraries
from bs4 import BeautifulSoup

# Reading the html text we want to parse
text = "<html> <head><title> Welcome </title></head><body><h1>This is a test page</h1></body></html>"

# creating a soup
soup = BeautifulSoup(text,"html.parser")

# printing the content in h1 tag
print(f"Content of h1 tag is: {soup.h1}")

# clearing the content of the tag
soup.h1.clear()

# printing the content in h1 tag after clearing
print(f"Content of h1 tag after clearing: {soup.h1}")
