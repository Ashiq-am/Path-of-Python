# Python3 code to demonstrate working of
# Add custom dimension in Matrix
# Using zip() + list comprehension + "+" operator

# initializing list
test_list = [(5, 6), (1, 2), (7, 8), (9, 12)]

# printing original list
print("The original list is : " + str(test_list))

# initializing Column values
vals = [4, 5, 7, 3]

# Add custom dimension in Matrix
# Using zip() + list comprehension + "+" operator
res = [i + (j, ) for i, j in zip(test_list, vals)]

# printing result
print("The result after adding dimension : " + str(res))
