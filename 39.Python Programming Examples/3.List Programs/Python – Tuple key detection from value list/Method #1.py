# Python3 code to demonstrate
# Tuple key detection from value list
# using List comprehension

# Initializing list
test_list = [('Gfg', [1, 3, 4]), ('is', [5, 8, 10]), ('best', [11, 9, 2])]

# printing original list
print("The original list is : " + str(test_list))

# Initializing K
K = 4

# Tuple key detection from value list
# using List comprehension
res = [sub[0] for sub in test_list if K in sub[1]]

# printing result
print("The required key of list values : " + str(res))
