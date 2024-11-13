# Python3 code to demonstrate
# adding K to each element
# using map() + lambda

# initializing list
test_list = [4, 5, 6, 3, 9]

# printing original list
print ("The original list is : " + str(test_list))

# initializing K
K = 4

# using map() + lambda
# adding K to each element
res = list(map(lambda x : x + K, test_list))

# printing result
print ("The list after adding K to each element : " + str(res))
