soup = BeautifulSoup(webpage.content, "lxml",
					parse_only = SoupStrainer(
					'span', class_ = 'mw-headline'))

print(soup.prettify())
