from bs4 import BeautifulSoup

# HTML element
input = b'''<html>
<meta charset="iso-8859-8"/>
<body>
<h1>\xa2\xf6`\xe0</h1>
</body>
</html>'''

# parsing content
soup = BeautifulSoup(input,"html.parser")

print(soup.prettify("iso-8859-8"))
