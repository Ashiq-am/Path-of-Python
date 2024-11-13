# Python3 code to demonstrate
# associate value in list
# using map() + lambda

# initializing list
test_list = [1, 4, 5, 8, 3, 10]

# initializing value to associate
val = 'geeks'

# printing the original list
print ("The original list is : " + str(test_list))

# printing value
print ("The value to be attached to each value : " + str(val))

# using map() + lambda
# associate value in list
res = list(map(lambda i: (i, val), test_list))

# printing result
print ("The modified attached list is : " + str(res))
