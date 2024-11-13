# Python3 code to demonstrate
# Tuple key detection from value list
# using filter() + lambda

# Initializing list
test_list = [('Gfg', [1, 3, 4]), ('is', [5, 8, 10]), ('best', [11, 9, 2])]

# printing original list
print("The original list is : " + str(test_list))

# Initializing K
K = 4

# Tuple key detection from value list
# using filter() + lambda
res = list(filter(lambda sub, ele=K: ele in sub[1], test_list))

# printing result
print("The required key of list values : " + str(res[0][0]))
