# Python3 code to demonstrate working of
# Nearest K Sort
# Using sorted() + abs() + lambda

# initializing list
test_list = [6, 7, 4, 11, 17, 8, 3]

# printing original list
print("The original list is : " + str(test_list))

# initializing K
K = 10

# sorted() used to perform sorting, lambda function to get logic
res = sorted(test_list, key=lambda ele: abs(ele - K))

# printing result
print("Sorted List : " + str(res))
