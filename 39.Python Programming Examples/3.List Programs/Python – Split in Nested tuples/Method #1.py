# Python3 code to demonstrate working of
# Split in Nested tuples
# Using list comprehension + unpack operator

# initializing list
test_list = [(3, ('Gfg', 'best')), (10, ('CS', 'good')), (7, ('Gfg', 'better'))]

# printing original list
print("The original list is : " + str(test_list))

# Split in Nested tuples
# Using list comprehension + unpack operator
res = [[a, *b] for a, b in test_list]

# printing result
print("The splitted elements : " + str(res))
