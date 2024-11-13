# get length of first tag only
for tag in soup.findAll(True):
	print(tag.name, " : ", len(soup.find(tag.name).text))
	break
