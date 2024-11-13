# display tables
for i in rows:
	table_data = i.find_all('td')
	data = [j.text for j in table_data]
	print(data)
