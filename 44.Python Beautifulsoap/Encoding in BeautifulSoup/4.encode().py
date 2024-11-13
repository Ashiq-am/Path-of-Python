from bs4 import BeautifulSoup

# HTML element
input = b"<html><head></head><body><h1>\xa2\xf6`\xe0</h1></body></html>"

# parsing content
soup = BeautifulSoup(input)

print("Content :",soup.h1.string)

print("Encoding method :",soup.original_encoding)

print("After explicit encoding :",soup.html.encode("iso-8859-8"))
