# Python3 code to demonstrate
# to check for strictly increasing list
# using reduce() + lambda

# initializing list
test_list = [1, 4, 5, 7, 8, 10]

# printing original lists
print ("Original list : " + str(test_list))

# using reduce() + lambda
# to check for strictly increasing list
res = bool(lambda test_list: reduce(lambda i, j: j if
				i < j else 9999, test_list) != 9999)

# printing result
print ("Is list strictly increasing ? : " + str(res))
