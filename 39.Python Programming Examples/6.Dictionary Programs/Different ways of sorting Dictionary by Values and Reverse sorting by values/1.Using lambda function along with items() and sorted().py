# Python program to sort dictionary
# by value using lambda function

# Initialize a dictionary
my_dict = {2: 'three',
		1: 'two'}

# Sort the dictionary
sorted_dict = sorted(
my_dict.items(),
key = lambda kv: kv[1])

# Print sorted dictionary
print("Sorted dictionary is :",
	sorted_dict)
