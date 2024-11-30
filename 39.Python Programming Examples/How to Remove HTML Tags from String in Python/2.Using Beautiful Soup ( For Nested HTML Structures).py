from bs4 import BeautifulSoup

# Sample string with HTML tags
s1 = "<h1>Welcome to <b>Python Programming</b></h1>"

# Removing HTML tags using Beautiful Soup
soup = BeautifulSoup(s1, "html.parser")
s2 = soup.get_text()
print(s2)