# Python3 code to demonstrate
# convert list of lists to list of sets
# using map() + set

# initializing list
test_list = [[1, 2, 1], [1, 2, 3], [2, 2, 2, 2], [0]]

# printing original list
print("The original list of lists : " + str(test_list))

# using map() + set
res = list(map(set, test_list))

# print result
print("The converted list of sets : " + str(res))
