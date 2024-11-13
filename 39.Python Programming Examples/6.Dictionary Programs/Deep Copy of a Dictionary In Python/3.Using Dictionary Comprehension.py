import copy

# original dictionary
dict = {
	'website': 'GeeksforGeeks',
	'topics': ['Algorithms', 'DSA', 'Python', 'ML']
}

# deep copy using dictionary comprehension
result = {key: copy.deepcopy(value) for key, value in dict.items()}

# modifying the original data to demonstrate the independence of the deep copy
dict['website'] = 'GFG'

# printing the original and deep copied data
print("Original Dictionary:")
print(dict)

print("\nDeep Copied Dictionary:")
print(result)
