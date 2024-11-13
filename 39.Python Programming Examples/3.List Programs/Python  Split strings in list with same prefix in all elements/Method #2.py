# Python3 code to demonstrate
# Split strings in list
# Using map() + slicing + lambda

# initializing list
test_list = ['Rs.25', 'Rs.100', 'Rs.143', 'Rs.12', 'Rs.4010']

# printing original list
print("The original list : " + str(test_list))

# using map() + slicing + lambda
# Split strings in list
res = list(map(lambda sub: sub[3:], test_list))

# print result
print("The list after string slicing : " + str(res))
