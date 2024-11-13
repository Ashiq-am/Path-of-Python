# Python program to sort dictionary
# by value using sorted() and get()

# Initialize a dictionary
my_dict = {'red': '# FF0000', 'green': '# 008000',
		'black': '# 000000', 'white': '# FFFFFF'}

# Sort and print dictionary
print("Sorted dictionary is :")
for w in sorted(my_dict, key = my_dict.get):
	print(w, my_dict[w])
