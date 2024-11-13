# Python3 code to demonstrate working of
# Replace value by Kth index value in Dictionary List
# Using loop + isinstance()

# initializing list
test_list = [{'gfg': [5, 7, 9, 1], 'is': 8, 'good': 10},
			{'gfg': 1, 'for': 10, 'geeks': 9},
			{'love': 3, 'gfg': [7, 3, 9, 1]}]

# printing original list
print("The original list is : " + str(test_list))

# initializing K
K = 2

# initializing Key
key = "gfg"

for sub in test_list:

	# using isinstance() to check for list
	if isinstance(sub[key], list):
		sub[key] = sub[key][K]

# printing result
print("The Modified Dictionaries : " + str(test_list))
