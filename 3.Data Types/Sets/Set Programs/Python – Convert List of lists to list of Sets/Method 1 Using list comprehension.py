# python3 program to convert list
# of lists to a list of sets


# initializing list
test_list = [[1, 2, 1], [1, 2, 3], [2, 2, 2, 2], [0]]

# printing original list
print("The original list of lists : " + str(test_list))

# using list comprehension
# convert list of lists to list of sets
res = [set(ele) for ele in test_list]

# print result
print("The converted list of sets : " + str(res))
