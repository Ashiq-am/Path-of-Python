# declaring string variables with dictionary
dct = {'str1': 'at',
	'str2': 'GeeksforGeeks',
	'str3': 'Understanding',
	'str4': '%s'}

# concatenating strings
final_str = "%(str3)s %(str4)s %(str1)s %(str2)s" % dct

# printing the final string
print("Concatenating multiple strings using Python '%s' operator:\n")
print(final_str)
