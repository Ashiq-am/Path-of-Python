# original dictionary
input_dict = {
	'website': 'GeeksforGeeks',
	'topics': ['Algorithms', 'DSA', 'Python', 'ML']
}

# deep copy using the dict() constructor
result = dict(input_dict)

# modifying the original data
input_dict['website'] = 'GFG'

# printing the original and deep copied data
print("Original Dictionary:")
print(input_dict)

print("\nDeep Copied Dictionary:")
print(result)
