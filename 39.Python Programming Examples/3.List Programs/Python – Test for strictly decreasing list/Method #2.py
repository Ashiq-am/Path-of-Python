# Python 3 code to demonstrate
# Test for strictly decreasing list
# using reduce() + lambda

# initializing list
test_list = [10, 8, 7, 5, 4, 1]

# printing original lists
print ("Original list : " + str(test_list))

# using reduce() + lambda
# Test for strictly decreasing list
res = bool(lambda test_list: reduce(lambda i, j: j if i > j else 9999, test_list) != 9999)

# printing result
print ("Is list strictly decreasing ? : " + str(res))
