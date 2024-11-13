# Initialising a dictionary
my_dict = {'red': '#FF0000', 'green': '#008000',
		'black': '#000000', 'white': '#FFFFFF'}

# Sorting dictionary in one line
sorted_dict = dict(sorted(my_dict .items()))

# Printing sorted dictionary
print("Sorted dictionary is : ")
for elem in sorted(sorted_dict.items()):
	print(elem[0], " ::", elem[1])
