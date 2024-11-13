# Python code to demonstrate
# sum of squares
# using reduce() + lambda

# initializing list
test_list = [3, 5, 7, 9, 11]

# printing original list
print ("The original list is : " + str(test_list))

# using reduce() + lambda
# sum of squares
res = reduce(lambda i, j: i + j * j, [test_list[:1][0]**2]+test_list[1:])

# printing result
print ("The sum of squares of list is : " + str(res))
