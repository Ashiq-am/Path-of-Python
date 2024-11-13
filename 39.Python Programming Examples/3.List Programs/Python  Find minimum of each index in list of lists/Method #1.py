# Python3 code to demonstrate
# Minimum index value
# using min() + list comprehension + zip()

# initializing list
test_list = [[3, 7, 6], [1, 3, 5], [9, 3, 2]]

# printing original list
print("The original list : " + str(test_list))

# using min() + list comprehension + zip()
# Minimum index value
res = [min(idx) for idx in zip(*test_list)]

# print result
print("The Minimum of each index list is : " + str(res))
