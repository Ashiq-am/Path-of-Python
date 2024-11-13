# Python3 code to demonstrate
# Record Value list Minimum
# using map() + lambda + min()

# initializing list
test_list = [('key1', [3, 4, 5]), ('key2', [1, 4, 2]), ('key3', [9, 3])]

# printing original list
print("The original list : " + str(test_list))

# using map() + lambda + min()
# Record Value list Minimum
res = list(map(lambda x: (x[0], min(x[1])), test_list))

# print result
print("The list tuple attribute minimum is : " + str(res))
