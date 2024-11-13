# embedding html document inyto BeautifulSoup variable
soup = BeautifulSoup(ht_doc, 'html.parser')

# assigning head element of BeautiulSoup-assigned Variable
htag=soup.head

# iterating through child in descendants of htag variable
for child in htag.descendants:
	print(child)
