import bs4


sibling_of_soup = bs4.BeautifulSoup("<a><b>CPPSecrets</b><c><strong>\
C++ Python Professional HandBook Guide</strong></b></a>",'lxml')

# Implementing Navigation on sibling
print(sibling_of_soup.c.next_sibling)
