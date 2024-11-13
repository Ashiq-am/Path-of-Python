# Python3 code to demonstrate working of
# Key with Maximum element at Kth index
# in Dictionary Value List Using max()
# + generator expression

# initializing dictionary
test_dict = {'Gfg': [4, 6, 8, 2, 5, 6],
			'is': [1],
			'best': [2, 3, 4, 10],
			'for': [4, 5, 2, 1],
			'geeks': [2, 10, 1, 10]}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# initializing K
K = 3

# sorted sorting all the values in reverse order
# Maximum element is found at 1st position
# getting maximum
temp = max(test_dict[key][K] if K < len(
	test_dict[key]) else -1 for key in test_dict)

# getting all keys with maximum.
res = []
for key in test_dict:
	if K < len(test_dict[key]) and test_dict[key][K] == temp:
		res.append(key)

# printing result
print("The extracted key : " + str(res))
