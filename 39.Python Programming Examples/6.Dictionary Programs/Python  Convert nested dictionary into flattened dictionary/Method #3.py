# Python code to demonstrate
# conversion of nested dictionary
# into flattened dictionary

my_map = {"a" : 1,
		"b" : {
			"c": 2,
			"d": 3,
			"e": {
				"f":4,
				6:"a",
				5:{"g" : 6},
				"l":[1,"two"]
			}
		}}

# Expected Output
# {'a': 1, 'b_c': 2, 'b_d': 3, 'b_e_f': 4, 'b_e_6': 'a', 'b_e_5_g': 6, 'b_e_l': [1, 'two']}


ini_dict = {'geeks': {'Geeks': {'for': 7}},
			'for': {'geeks': {'Geeks': 3}},
			'Geeks': {'for': {'for': 1, 'geeks': 4}}}

# Expected Output
# {‘Geeks_for_geeks’: 4, ‘for_geeks_Geeks’: 3, ‘Geeks_for_for’: 1, ‘geeks_Geeks_for’: 7}

def flatten_dict(pyobj, keystring=''):
	if type(pyobj) == dict:
		keystring = keystring + '_' if keystring else keystring
		for k in pyobj:
			yield from flatten_dict(pyobj[k], keystring + str(k))
	else:
		yield keystring, pyobj

print("Input : %s\nOutput : %s\n\n" %
	(my_map, { k:v for k,v in flatten_dict(my_map) }))

print("Input : %s\nOutput : %s\n\n" %
	(ini_dict, { k:v for k,v in flatten_dict(ini_dict) }))
