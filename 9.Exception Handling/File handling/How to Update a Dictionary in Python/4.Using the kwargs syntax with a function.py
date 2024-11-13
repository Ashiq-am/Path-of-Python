# Define a function that takes a dictionary and **kwargs
def update_dict(input_dict, **kwargs):
	# Update the input_dict with the provided keyword arguments
	input_dict.update(kwargs)

# Create an initial dictionary
dict = {'a': 1, 'b': 2}

# Call the update_dict function with **kwargs to update the dictionary
update_dict(dict, c=3, d=4)

# Print the updated dictionary
print(dict)
