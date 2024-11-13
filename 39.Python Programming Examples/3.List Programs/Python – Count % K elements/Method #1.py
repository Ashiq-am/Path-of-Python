# Python 3 code to demonstrate
# Count % K elements
# using sum() + generator expression

# initializing list
test_list = [3, 5, 1, 6, 7, 9]

# printing original list
print ("The original list is : " + str(test_list))

# initializing K
K = 3

# using sum() + generator expression
# to get count of elements matching condition
# Count % K elements
res = sum(1 for i in test_list if i % K != 0)

# printing result
print ("The number of % K elements: " + str(res))
