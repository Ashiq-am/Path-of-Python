# Python3 code to demonstrate
# column summation of list of tuple
# using list comprehension + zip()

# initializing list
test_list = [[(1, 4), (2, 3), (5, 2)],
			[(3, 7), (1, 9), (10, 5)]]

# printing original list
print("The original list : " + str(test_list))

# using list comprehension + zip()
# columnn summation of list of tuple
res = [tuple(sum(j) for j in zip(*i))
			for i in zip(*test_list)]

# print result
print("The summation of columns of tuple list : " + str(res))
