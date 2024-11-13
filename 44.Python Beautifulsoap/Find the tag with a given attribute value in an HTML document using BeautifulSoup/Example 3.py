# importing module
from bs4 import BeautifulSoup

markup = """<html><head><title>Welcome to geeksforgeeks</title></head>
<body>
<p class="title"><b>Geeks</b></p>

<p class="gfg">geeksforgeeks a computer science portal for geeks
</body>
"""
soup = BeautifulSoup(markup, 'html.parser')

# finding the tag with the class attribute
div_bs4 = soup.find(class_="gfg")

print(div_bs4.name)
