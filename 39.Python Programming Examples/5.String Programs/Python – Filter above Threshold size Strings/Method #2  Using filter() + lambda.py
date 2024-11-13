# Python3 code to demonstrate working of
# Filter above Threshold size Strings
# using filter() + lambda

# initialize list
test_list = ['gfg', 'is', 'best', 'for', 'geeks']

# printing original list
print("The original list : " + str(test_list))

# initialize Threshold
thres = 4

# Filter above Threshold size Strings
# using filter() + lambda
res = list(filter(lambda ele: len(ele) >= thres, test_list))

# printing result
print("The above Threshold size strings are : " + str(res))
