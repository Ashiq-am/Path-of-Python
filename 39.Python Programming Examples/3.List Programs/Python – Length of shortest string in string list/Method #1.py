# Python3 code to demonstrate working of
# Minimum String length
# using min() + generator expression

# initialize list
test_list = ['gfg', 'is', 'best']

# printing original list
print("The original list : " + str(test_list))

# Minimum String length
# using min() + generator expression
res = min(len(ele) for ele in test_list)

# printing result
print("Length of minimum string is : " + str(res))
