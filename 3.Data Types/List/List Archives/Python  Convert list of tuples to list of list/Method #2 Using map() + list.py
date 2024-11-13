# Python3 code to demonstrate
# convert list of tuples to list of list
# using map() + list

# initializing list
test_list = [(1, 2), (3, 4), (5, 6)]

# printing original list
print("The original list of tuples : " + str(test_list))

# using map() + list
# convert list of tuples to list of list
res = list(map(list, test_list))

# print result
print("The converted list of list : " + str(res))
