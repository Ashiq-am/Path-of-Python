# Python3 code to demonstrate
# Records element list Maximum
# using map() + lambda + max()

# initializing list
test_list = [('key1', [3, 4, 5]), ('key2', [1, 4, 2]), ('key3', [9, 3])]

# printing original list
print("The original list : " + str(test_list))

# using map() + lambda + max()
# Records element list Maximum
res = list(map(lambda x: (x[0], max(x[1])), test_list))

# print result
print("The list tuple attribute maximum is : " + str(res))
