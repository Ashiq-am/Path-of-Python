#opening file in read mode
with open(jsonFile, 'r') as file:
	#parsing the json file
	data = json.load(file)
