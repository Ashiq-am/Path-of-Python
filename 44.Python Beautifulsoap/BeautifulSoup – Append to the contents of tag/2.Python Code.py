# Python program to append to the contents of tag

# Importing library
from bs4 import BeautifulSoup

# Opening and reading the html file
file = open("gfg.html", "r")
contents = file.read()

soup = BeautifulSoup(contents, "lxml")

# Appending to the contents of 'title' tag in html file
print("Current content in title tag is:-")
print(soup.title)
soup.title.append("Using BS")
print("Content after appending is:-")
print(soup.title)

print("\n")

# Appending to the contents of 'h1' tag in html file
print("Current content in heading h1 tag is:-")
print(soup.h1)
soup.h1.append("contents of tag")
print("Content after appending is:-")
print(soup.h1)

print("\n")

# Appending to the contents of 'p' tag in html file
print("Current content in paragraph p tag is:-")
print(soup.p)
soup.p.append("BeautifulSoup library")
print("Content after appending is:-")
print(soup.p)

print("\n")

# Appending to the contents of 'a' tag in html file
print("Current content in anchor a tag is:-")
print(soup.a)
soup.a.append("Geeks Website")
print("Content after appending is:-")
print(soup.a)

# Code to save the changes in 'output.html' file
savechanges = soup.prettify("utf-8")
with open("output.html", "wb") as file:
	file.write(savechanges)
