# Python3 code to demonstrate
# Search in Matrix
# using any() + list comprehension

# initializing list
test_list = [[4, 5, 6],
			[10, 2, 13],
			[1, 11, 18]]

# printing original list
print("The original list : " + str(test_list))

# using any() + list comprehension
# to Search in Matrix
res = any(13 in sub for sub in test_list)

# printing result
print("Is 13 present in Matrix ? : " + str(res))
