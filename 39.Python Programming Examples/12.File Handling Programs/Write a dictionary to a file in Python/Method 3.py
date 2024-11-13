details = {'Name': "Bob", 'Age' :28}

with open('file.txt','w') as data:
	data.write(str(details))
