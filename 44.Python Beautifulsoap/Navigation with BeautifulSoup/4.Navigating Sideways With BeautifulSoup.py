from bs4 import BeautifulSoup
sibling_soup = BeautifulSoup("<a><b>Geeks For Geeks</b><c><strong>The \
Biggest Online Tutorials Library, It's all Free</strong></b></a>")

# to retreive next sibling of b tag
print(sibling_soup.b.next_sibling)

# for retreiving previous sibling of c tag
print(sibling_soup.c.previous_sibling)
