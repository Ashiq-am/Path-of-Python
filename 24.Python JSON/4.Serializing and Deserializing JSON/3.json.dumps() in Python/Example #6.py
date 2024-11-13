import json

Dictionary ={'c':'Welcome', 'b':'to',
			'a':'Geeks'}

json_string = json.dumps(Dictionary,
						indent = 6,
						separators =(". ", " = "),
						sort_keys = True)

print('Equivalent json string of dictionary:',
	json_string)
