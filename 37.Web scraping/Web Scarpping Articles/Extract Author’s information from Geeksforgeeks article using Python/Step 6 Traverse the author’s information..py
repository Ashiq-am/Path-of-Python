# traverse information of auther
name = soup.find(
	'div', class_='mdl-cell mdl-cell--9-col mdl-cell--12-col-phone textBold medText').get_text()


author_info = []
for item in soup.find_all('div', class_='mdl-cell mdl-cell--9-col mdl-cell--12-col-phone textBold'):
	author_info.append(item.get_text())

print("Author name :")
print(name)
print("Author information :")
print(author_info)
