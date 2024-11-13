# Python3 code to demonstrate working of
# Extract K sized strings
# using filter() + lambd

# initialize list
test_list = ['gfg', 'is', 'best', 'for', 'geeks']

# printing original list
print("The original list : " + str(test_list))

# initialize K
K = 3

# Extract K sized strings
# using filter() + lambda
res = list(filter(lambda ele: len(ele) == K, test_list))

# printing result
print("The K sized strings are : " + str(res))
