soup = BeautifulSoup(ht_doc, 'html.parser')
for string in soup.strings :
	print(repr(string))
