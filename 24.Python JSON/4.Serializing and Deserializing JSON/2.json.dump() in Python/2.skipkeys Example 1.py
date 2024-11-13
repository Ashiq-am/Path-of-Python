# dictionary to be dumped
d ={'lang':'??? ????'}

with open('myfile.json', 'w', encoding ='utf8') as json_file:
	json.dump(d, json_file, ensure_ascii = False)
