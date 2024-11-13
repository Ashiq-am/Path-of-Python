# Python program to sort the items alphabetically from given dictionary

# initialising _dictionary
dict = {'key1' : 'AGeek', 'key2' : 'For', 'key3': 'IsGeeks', 'key4': 'ZGeeks'}

# printing iniial_dictionary
print ("Original dictionary", str(dict))

# getting items in sorted order
print ("\nItems in sorted order")
for key in sorted(dict):
	print (dict[key])
