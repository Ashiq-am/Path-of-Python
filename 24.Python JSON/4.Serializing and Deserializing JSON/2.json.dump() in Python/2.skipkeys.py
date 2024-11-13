import json

# python object(dictionary) to be dumped
dict1 ={
	('addresss', 'street'):'Brigade road',
}

# the json file where the output must be stored
out_file = open("myfile.json", "w")

json.dump(dict1, out_file, indent = 6)

out_file.close()
