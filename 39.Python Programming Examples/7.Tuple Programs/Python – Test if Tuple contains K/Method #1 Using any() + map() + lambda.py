# Python3 code to demonstrate working of
# Test if Tuple contains K
# using any() + map() + lambda

# initialize tuple
test_tup = (10, 4, 5, 6, 8)

# printing original tuple
print("The original tuple : " + str(test_tup))

# initialize K
K = 6

# Test if Tuple contains K
# using any() + map() + lambda
res = any(map(lambda ele: ele is K, test_tup))

# printing result
print("Does tuple contain any K value ? : " + str(res))
