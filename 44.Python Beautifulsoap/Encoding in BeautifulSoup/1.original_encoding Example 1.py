from bs4 import BeautifulSoup

# HTML element with content
h1 = b"<h1>Hello world!!</h1>"

# parsing with html parser
parsed = BeautifulSoup(h1, "html.parser")

# tag found
print("Tag foud :", parsed.h1.name)

# the content inside the tag
print("Content :", parsed.h1.string)

# the encoded method
print("Encoding method :", parsed.original_encoding)
