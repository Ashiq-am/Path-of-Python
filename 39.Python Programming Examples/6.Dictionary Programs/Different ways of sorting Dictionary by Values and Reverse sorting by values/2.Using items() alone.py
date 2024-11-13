# Python program to sort dictionary
# by value using item function

# Initialize a dictionary
my_dict = {'c': 3,
		'a': 1,
		'd': 4,
		'b': 2}

# Sorting dictionary
sorted_dict = sorted([(value, key)
for (key, value) in my_dict.items()])

# Print sorted dictionary
print("Sorted dictionary is :")
print(sorted_dict)
