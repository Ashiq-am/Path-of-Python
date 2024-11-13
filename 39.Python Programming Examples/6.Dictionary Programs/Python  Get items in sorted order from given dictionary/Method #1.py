# Python code to demonstrate
# to get sorted items from dictionary

# initialising _dictionary
ini_dict = {'a' : 'akshat', 'b' : 'bhuvan', 'c': 'chandan'}

# printing iniial_dictionary
print ("iniial_dictionary", str(ini_dict))

# getting items in sorted order
print ("\nItems in sorted order")
for key in sorted(ini_dict):
	print (ini_dict[key])
