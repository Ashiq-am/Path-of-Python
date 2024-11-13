from bs4 import BeautifulSoup

soup_lxml = BeautifulSoup("<li></p>", "lxml")

print(soup_lxml)
