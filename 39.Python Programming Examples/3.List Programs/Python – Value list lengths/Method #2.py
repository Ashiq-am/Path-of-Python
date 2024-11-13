# Python3 code to demonstrate
# Value list lengths
# using map() + lambda + len()

# initializing list
test_list = [('key1', [3, 4, 5]), ('key2', [1, 4, 2]), ('key3', [9, 3])]

# printing original list
print("The original list : " + str(test_list))

# using map() + lambda + len()
# Value list lengths
res = list(map(lambda x: (x[0], len(x[1])), test_list))

# print result
print("The list tuple attribute length is : " + str(res))
