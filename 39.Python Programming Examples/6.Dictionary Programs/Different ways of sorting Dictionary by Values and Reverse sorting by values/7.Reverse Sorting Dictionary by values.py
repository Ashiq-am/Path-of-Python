# Python program to sort dictionary
# by value using sorted setting
# reverse parameter to true

# Initialize a dictionary
my_dict = {'red': '# FF0000', 'green': '# 008000',
		'black': '# 000000', 'white': '# FFFFFF'}

# Sort and print the dictionary
print("Sorted dictionary is :")
for w in sorted(my_dict, key = my_dict.get,reverse = True):
	print(w, my_dict[w])
