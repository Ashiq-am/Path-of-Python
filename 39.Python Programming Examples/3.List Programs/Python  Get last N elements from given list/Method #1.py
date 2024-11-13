# Python3 code to demonstrate
# Get last N elements from list
# using list slicing

# initializing list
test_list = [4, 5, 2, 6, 7, 8, 10]

# printing original list
print("The original list : " + str(test_list))

# initializing N
N = 5

# using list slicing
# Get last N elements from list
res = test_list[-N:]

# print result
print("The last N elements of list are : " + str(res))
