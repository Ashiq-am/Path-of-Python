# Python3 code to demonstrate working of
# Extracting length of longest string in list
# using max() + generator expression

# initialize list
test_list = ['gfg', 'is', 'best']

# printing original list
print("The original list : " + str(test_list))

# Extracting length of longest string in list
# using max() + generator expression
res = max(len(ele) for ele in test_list)

# printing result
print("Length of maximum string is : " + str(res))
