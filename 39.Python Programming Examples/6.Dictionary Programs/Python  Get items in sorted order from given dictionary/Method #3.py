# Python code to demonstrate
# to get sorted items from dictionary

import operator

# initialising _dictionary
ini_dict = {'a' : 'akshat', 'b' : 'bhuvan', 'c': 'chandan'}

# printing iniial_dictionary
print("iniial_dictionary", str(ini_dict))

# getting items in sorted order
print ("\nItems in sorted order")
for key, value in sorted(ini_dict.iteritems(),
						key = operator.itemgetter(1),
						reverse = False):
	print(key, " ", value)
