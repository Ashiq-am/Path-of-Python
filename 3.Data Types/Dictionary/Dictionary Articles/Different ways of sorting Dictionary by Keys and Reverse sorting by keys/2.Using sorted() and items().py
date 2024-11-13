# Initialising dictionary
my_dict = {2: 'three', 1: 'two', 4: 'five', 3: 'four'}

# Sorting dictionary
sorted_dict = sorted(my_dict.items())

# Printing sorted dictionary
print("Sorted dictionary using sorted() and items() is :")
for k, v in sorted_dict:
	print(k, v)
