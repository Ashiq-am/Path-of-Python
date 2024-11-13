# Python 3 code to demonstrate
# to get count of elements matching condition
# using sum() + generator expression

# initializing list
test_list = [3, 5, 1, 6, 7, 9]

# printing original list
print ("The original list is : " + str(test_list))

# using sum() + generator expression
# to get count of elements matching condition
# checks for odd
res = sum(1 for i in test_list if i % 2 != 0)

# printing result
print ("The number of odd elements: " + str(res))
