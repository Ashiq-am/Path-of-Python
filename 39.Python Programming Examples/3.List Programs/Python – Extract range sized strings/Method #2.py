# Python3 code to demonstrate working of
# Range length Strings extraction
# using filter() + lambd

# initialize list
test_list = ['gfg', 'is', 'best', 'for', 'geeks']

# printing original list
print("The original list : " + str(test_list))

# initialize i, j
i, j = 2, 3

# Range length Strings extraction
# using filter() + lambda
res = list(filter(lambda ele: len(ele) >= i and len(ele) <= j, test_list))

# printing result
print("The range sized strings are : " + str(res))
