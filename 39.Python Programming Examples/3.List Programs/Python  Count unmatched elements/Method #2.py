# Python 3 code to demonstrate
# Count unmatched elements
# using len() + generator expression

# initializing list
test_list = [3, 5, 1, 6, 7, 9]

# printing original list
print ("The original list is : " + str(test_list))

# using len() + generator expression
# Count unmatched elements
# checks for odd
res = len(list(i for i in test_list if not i % 2 != 0))

# printing result
print ("The number of non-odd elements: " + str(res))
