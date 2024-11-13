# Python code to demonstrate
# changing all keys of dictionary
# corresponding to list using zip()

# inititialising dictionary
ini_dict = {'nikhil': 1, 'vashu' : 5,
			'manjeet' : 10, 'akshat' : 15}

# initialising list
ini_list = ['a', 'b', 'c', 'd']

# printing initial json
print ("initial 1st dictionary", ini_dict)

# changing keys of dictionary
final_dict = dict(zip(ini_list, list(ini_dict.values())))

# printing final result
print ("final dictionary", str(final_dict))
