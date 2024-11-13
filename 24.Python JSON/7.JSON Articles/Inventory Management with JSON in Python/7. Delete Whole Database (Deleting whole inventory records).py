def delete_all():
	fd = open("data.json", 'r')
	txt = fd.read()
	data = json.loads(txt)
	fd.close()
	data = {} # Replacing Data with NULL Dictionary
	js = json.dumps(data)
	fd = open("data.json", 'w')
	fd.write(js)
	fd.close()
