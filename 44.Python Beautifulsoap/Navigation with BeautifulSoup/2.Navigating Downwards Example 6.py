soup = BeautifulSoup(ht_doc, 'html.parser')
htag = soup.head
print(htag.string)
