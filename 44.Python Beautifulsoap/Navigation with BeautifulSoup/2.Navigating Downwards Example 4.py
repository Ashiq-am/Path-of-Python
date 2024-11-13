soup = BeautifulSoup(ht_doc, 'html.parser')

# assigning head tag of BeautifulSoup variable
hTag = soup.head
print(hTag)

# retreiving contents of BeautifulSoup variable
print(hTag.contents)
