# Python3 code to demonstrate
# List lengths as record attribute
# using map() + lambda + len()

# initializing list
test_list = [('key1', [3, 4, 5]), ('key2', [1, 4, 2]), ('key3', [9, 3])]

# printing original list
print("The original list : " + str(test_list))

# using map() + lambda + len()
# List lengths as record attribute
res = list(map(lambda x: (x[0], len(x[1])), test_list))

# print result
print("The list tuple attribute lengths is : " + str(res))
