# Python3 code to demonstrate working of
# Trim tuples by K
# Using list comprehension + slicing

# initializing list
test_list = [(5, 3, 2, 1, 4), (3, 4, 9, 2, 1),
			(9, 1, 2, 3, 5), (4, 8, 2, 1, 7)]

# printing original list
print("The original list is : " + str(test_list))

# initializing K
K = 2

# one-liner approach to solve problem
res = [tuple(list(ele)[K: len(ele) - K]) for ele in test_list]

# printing result
print("Converted Tuples : " + str(res))
