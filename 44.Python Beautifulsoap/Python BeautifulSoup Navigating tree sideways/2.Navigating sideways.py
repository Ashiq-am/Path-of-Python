# For importing BeautifulSoup
import bs4


# initiating variable of BeautifulSoup
sibling_of_soup = bs4.BeautifulSoup("<a><b>CPPSecrets</b><c><strong>\
C++ Python Professional HandBook Guide</strong></b></a>", 'lxml')

# To print contents in the initiated BeautifulSoup
print(sibling_of_soup.prettify())
