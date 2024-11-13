# Python3 code to demonstrate
# Summation of list as tuple attribute
# using map() + lambda + sum()

# initializing list
test_list = [('key1', [3, 4, 5]), ('key2', [1, 4, 2]), ('key3', [9, 3])]

# printing original list
print("The original list : " + str(test_list))

# using map() + lambda + sum()
# Summation of list as tuple attribute
res = list(map(lambda x: (x[0], sum(x[1])), test_list))

# print result
print("The list tuple attribute summation is : " + str(res))
