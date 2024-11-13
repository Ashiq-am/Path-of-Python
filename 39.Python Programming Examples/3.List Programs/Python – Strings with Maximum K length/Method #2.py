# Python3 code to demonstrate working of
# Extract Strings with Maximum K length
# using filter() + lambd

# initialize list
test_list = ['gfg', 'is', 'best', 'for', 'geeks']

# printing original list
print("The original list : " + str(test_list))

# initialize K
K = 3

# Extract Strings with Maximum K length
# using filter() + lambda
res = list(filter(lambda ele: len(ele) <= K, test_list))

# printing result
print("The maximum K sized strings are : " + str(res))
