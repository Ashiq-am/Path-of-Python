import bs4


sibling_soup = bs4.BeautifulSoup("<a><b>Welcome to Geekforgeeks</b>\
<c>Hello geeks</c></b></a>", 'html.parser')
print(sibling_soup.prettify())
