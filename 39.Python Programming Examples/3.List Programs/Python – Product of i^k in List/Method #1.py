# Python code to demonstrate
# Product of i ^ k in List
# using reduce() + lambda + pow()

# initializing list
test_list = [1, 3, 5, 7, 9, 11]

# printing original list
print ("The original list is : " + str(test_list))

# initializing K
K = 4

# using reduce() + lambda + pow()
# Product of i ^ k in List
res = reduce(lambda i, j: i * pow(j, K), [pow(test_list[:1][0], K)] + test_list[1:])

# printing result
print ("The product of i ^ k of list is : " + str(res))
