# traverse the station code
data = []
for item in soup.find("table", class_="extrtable").find_all('b'):
	data.append(item.get_text())
print(data[-1])
