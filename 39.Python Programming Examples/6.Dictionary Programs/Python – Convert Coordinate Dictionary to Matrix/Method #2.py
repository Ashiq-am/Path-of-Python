# Python3 code to demonstrate working of
# Convert Coordinate Dictionary to Matrix
# Using list comprehension

# initializing dictionary
test_dict = { (0, 1) : 4, (2, 2) : 6, (3, 1) : 7, (1, 2) : 10, (3, 2) : 11}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# Convert Coordinate Dictionary to Matrix
# Using list comprehension
temp_x, temp_y = map(max, zip(*test_dict))
res = [[test_dict.get((j, i), 0) for i in range(temp_y + 1)]
								for j in range(temp_x + 1)]

# printing result
print("The dictionary after creation of Matrix : " + str(res))
