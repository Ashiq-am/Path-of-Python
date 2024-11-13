import json

Dictionary ={(1, 2, 3):'Welcome', 2:'to',
			3:'Geeks', 4:'for',
			5:'Geeks', 6:float('nan')}

# If specified, separators should be
# an (item_separator, key_separator)tuple
# Items are seperated by '.' and key,
# values are seperated by '='
json_string = json.dumps(Dictionary,
						skipkeys = True,
						allow_nan = True,
						indent = 6,
						separators =(". ", " = "))

print('Equivalent json string of dictionary:',
	json_string)
