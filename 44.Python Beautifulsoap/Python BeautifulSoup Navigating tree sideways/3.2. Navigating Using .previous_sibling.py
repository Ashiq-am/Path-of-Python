import bs4

sibling_of_soup = bs4.BeautifulSoup("<a><b>CPPSecrets</b><c><strong> C++ Python Professional")

print(sibling_of_soup.c.previous_sibling)
print(sibling_of_soup.b.previous_sibling)
