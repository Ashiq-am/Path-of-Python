# Python3 code to demonstrate working of
# Threshold Size Greater Strings Frequency
# using filter() + lambda + len()

# initialize list
test_list = ['gfg', 'is', 'best', 'for', 'geeks']

# printing original list
print("The original list : " + str(test_list))

# initialize K
K = 3

# Threshold Size Greater Strings Frequency
# using filter() + lambda + len()
res = len(list(filter(lambda ele: len(ele) >= K, test_list)))

# printing result
print("The frequency of threshhold K sized strings are : " + str(res))
