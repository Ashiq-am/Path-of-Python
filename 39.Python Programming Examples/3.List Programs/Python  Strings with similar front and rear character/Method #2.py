# Python3 code to demonstrate working of
# Similar front and rear elements
# Using sum() + generator expression

# initialize list
test_list = ['gfg', 'is', 'best', 'treat']

# printing original list
print("The original list : " + str(test_list))

# Similar front and rear elements
# Using sum() + generator expression
res = sum(1 for ele in test_list if ele[0] == ele[-1])

# printing result
print("Total Strings with similar front and rear elements : " + str(res))
