# Python3 code to demonstrate
# Search in Matrix
# using any() + list comprehension

# initializing list
test_list = [[4, 5, 6],
			[10, 2, None],
			[1, 11, 18]]

# printing original list
print("The original list : " + str(test_list))

# using any() + list comprehension
# to Search in Matrix
res = any(None in sub for sub in test_list)

# printing result
print("Does Matrix contain None value ? : " + str(res))
