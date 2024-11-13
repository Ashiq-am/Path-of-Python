# Python3 code to demonstrate working of
# Length Conditional Concatenation
# Using join() + filter() + lambda + len()

# initializing lists
test_list = ["Gfg", 'is', "Best", 'for', 'CS', 'Everything']

# printing original list
print("The original list : " + str(test_list))

# initializing K
K = 2

# join() performing Concatenation of required strings
res = ''.join(filter(lambda ele: len(ele) > K, test_list))

# printing result
print("String after Concatenation : " + str(res))
