# Python3 code to demonstrate
# sum of squares
# using sum() + max()

# initializing list
test_list = [3, 5, 7, 9, 11]

# printing original list
print ("The original list is : " + str(test_list))

# using sum() + max()
# sum of squares
res = sum(map(lambda i : i * i, test_list))

# printing result
print ("The sum of squares of list is : " + str(res))
