# Python3 code to demonstrate working of
# Convert Coordinate Dictionary to Matrix
# Using loop + max() + list comprehension

# initializing dictionary
test_dict = { (0, 1) : 4, (2, 2) : 6, (3, 1) : 7, (1, 2) : 10, (3, 2) : 11}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# Convert Coordinate Dictionary to Matrix
# Using loop + max() + list comprehension
temp_x = max([cord[0] for cord in test_dict.keys()])
temp_y = max([cord[1] for cord in test_dict.keys()])
res = [[0] * (temp_y + 1) for ele in range(temp_x + 1)]

for (i, j), val in test_dict.items():
	res[i][j] = val

# printing result
print("The dictionary after creation of Matrix : " + str(res))
