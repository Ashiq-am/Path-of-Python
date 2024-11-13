# Python3 code to demonstrate
# convert list of strings to list of tuples
# Using map() + split() + tuple()

# initializing list
test_list = ['4, 1', '3, 2', '5, 3']

# printing original list
print("The original list : " + str(test_list))

# using map() + split() + tuple()
# convert list of strings to list of tuples
res = [tuple(map(int, sub.split(', '))) for sub in test_list]

# print result
print("The list after conversion to tuple list : " + str(res))
