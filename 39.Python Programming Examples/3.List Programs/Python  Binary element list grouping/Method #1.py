# Python3 code to demonstrate
# to perform binary list grouping
# using list comprehension

# initializing list
test_list = [["G", 0], ["F", 0], ["B", 2],
			["E", 2], ['I', 1], ['S', 1],
			['S', 2], ['T', 2], ['G', 0]]

# using list comprehension
# to perform binary list grouping
temp = set(map(lambda i : i[1], test_list))
res = [[j[0] for j in test_list if j[1] == i] for i in temp]

# printing result
print ("The grouped list is : " + str(res))
