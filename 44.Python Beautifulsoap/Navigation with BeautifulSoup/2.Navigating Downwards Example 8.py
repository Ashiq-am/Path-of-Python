# embedding HTML document in BeautifulSoup-assigned variable
soup = BeautifulSoup(ht_doc, 'html.parser')

# iterating through string in stripped_strings of
# BeautifulSoup assigned variable
for string in soup.stripped_strings :
	print(repr(string))
