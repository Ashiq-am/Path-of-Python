# Python3 code to demonstrate
# group flattening of list
# using list comprehension + list slicing

# initializing list of lists
test_list = [[1, 3], [3, 4], [6, 5], [4, 5], [7, 6], [7, 9]]

# printing original list
print("The original list : " + str(test_list))

# declaring K
K = 3

# using list comprehension + list slicing
# group flattening of list
res = [[i for sub in test_list[j : j + K] for i in sub]
				for j in range(0, len(test_list), K)]

# printing result
print("The grouped flattened list : " + str(res))
