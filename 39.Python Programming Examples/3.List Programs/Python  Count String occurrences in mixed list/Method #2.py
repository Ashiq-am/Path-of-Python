# Python3 code to demonstrate working of
# Check String occurrences in mixed list
# using sum() + isinstance() + generator expression

# initialize list
test_list = ['gfg', 1, True, 'is', 2, 'best']

# printing original list
print("The original list : " + str(test_list))

# Check String occurrences in mixed list
# using sum() + isinstance() + generator expression
res = sum(isinstance(ele, str) for ele in test_list)

# printing result
print("Number of strings in list : " + str(res))
