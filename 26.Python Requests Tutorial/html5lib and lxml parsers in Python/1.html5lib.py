from bs4 import BeautifulSoup

soup_html5lib = BeautifulSoup("<li></p>", "html5lib")

print(soup_html5lib)
