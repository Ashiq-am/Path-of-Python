import copy

# dictionary data
input_dict = {
	'website': 'GeeksforGeeks',
	'topics': ['Algorithms', 'DSA', 'Python', 'ML']
}

# using deepcopy from the copy module to create a deep copy
result = copy.deepcopy(input_dict)

# modifying the original data to demonstrate the independence of the deep copy
input_dict['website'] = 'GFG'

# printing the original and deep copied data
print("Original Dictionary:")
print(input_dict)

print("\nDeep Copied Dictionary:")
print(result)
