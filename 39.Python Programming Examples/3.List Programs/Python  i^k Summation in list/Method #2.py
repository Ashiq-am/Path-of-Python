# Python3 code to demonstrate
# i ^ k Summation in list
# using map() + sum() + pow()

# initializing list
test_list = [3, 5, 7, 9, 11]

# printing original list
print ("The original list is : " + str(test_list))

# initializing K
K = 4

# using map() + sum() + pow()
# i ^ k Summation in list
res = sum(map(lambda i : pow(i, K), test_list))

# printing result
print ("The sum of i ^ k of list is : " + str(res))
