import bs4


sibling_of_soup = bs4.BeautifulSoup("<a><b>CPPSecrets</b><c><strong>\
C++ Python Professional HandBook Guide</strong></b></a>",'lxml')

# printing contents in BeautifulSoup Variable
print(sibling_of_soup.b.next_sibling)
