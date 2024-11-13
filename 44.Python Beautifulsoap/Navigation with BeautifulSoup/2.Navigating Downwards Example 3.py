soup = BeautifulSoup(ht_doc, 'html.parser')

# retreiving b tag element
print(soup.body.b)

# retreiving a tag leement from BeautifulSoup assigned variable
print(soup.a)

# retreiving all elements tagged with a in ht_doc
print(soup.find_all("a"))
