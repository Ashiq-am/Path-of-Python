import json


# dictionary to be dumped
d ={
	'a':1,
	'x':float('nan')
}

with open('myfile.json', 'w', encoding ='utf8') as json_file:
	json.dump(d, json_file, allow_nan=True)
