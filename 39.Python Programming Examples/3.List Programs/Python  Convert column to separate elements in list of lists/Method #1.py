# Python3 code to demonstrate
# column to separate elements in list of lists
# using list slicing and list comprehension

# initializing list of list
test_list = [[1, 3, 4],
			[6, 2, 8],
			[9, 10, 5]]

# printing original list
print ("The original list is : " + str(test_list))

# using list slicing and list comprehension
# column to separate elements in list of lists
res = [i for nest_list in [[j[1 : ], [j[0]]]
		for j in test_list] for i in nest_list]

# printing result
print ("The list after colum shift is : " + str(res))
