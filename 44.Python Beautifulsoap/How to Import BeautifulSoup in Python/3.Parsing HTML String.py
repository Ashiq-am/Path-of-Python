# import module
from bs4 import BeautifulSoup

# HTML document
html_doc = """
<html>
<head>
<title>GeeksforGeeks</title>
</head>
<body>
<h1>Welcome to GFG!</h1>
<p>This is BeautifulSoup Example</p>
<ul>
  <li>Python</li>
  <li>Java</li>
  <li>C++</li>
</ul>
</body>
</html>
"""

# parsing HTML document
soup = BeautifulSoup(html_doc, 'html.parser')

# extracting details
title = soup.title
print(f"Title: {title.text}")
paragraph = soup.p
print(f"First Paragraph: {paragraph.text}")
list_items = soup.find_all('li')
print("List Items:")
for item in list_items:
    print(item.text)
