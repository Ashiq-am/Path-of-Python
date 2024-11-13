from bs4 import BeautifulSoup

# HTML element
input = b"<h1>\xa2\xf6`\xe0</h1>"

# parsing content
soup = BeautifulSoup(input, "html.parser", from_encoding="iso-8859-8")

print("Content :",soup.h1.string)

print("Encoding method :",soup.original_encoding)
