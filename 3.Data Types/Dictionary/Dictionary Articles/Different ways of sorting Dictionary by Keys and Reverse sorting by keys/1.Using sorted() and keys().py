# Initialising a dictionary
my_dict = {'c':3, 'a':1, 'd':4, 'b':2}

# Sorting dictionary
sorted_dict = my_dict.keys()
sorted_dict = sorted(sorted_dict)

# Printing sorted dictionary
print("Sorted dictionary using sorted() and keys() is : ")
for key in sorted_dict:
	print(key,':', my_dict[key])
