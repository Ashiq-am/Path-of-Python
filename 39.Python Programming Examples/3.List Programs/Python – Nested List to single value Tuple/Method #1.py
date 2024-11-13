# Python3 code to demonstrate working of
# Convert Nested List to 1 value Tuple
# Using list comprehension

# initializing list
test_list = [[5, 6], [4, 7, 10], [12], [9, 11]]

# printing original list
print("The original list is : " + str(test_list))

# Convert Nested List to 1 value Tuple
# Using list comprehension
res = [(ele, ) for sub in test_list for ele in sub]

# printing result
print("The converted container : " + str(res))
