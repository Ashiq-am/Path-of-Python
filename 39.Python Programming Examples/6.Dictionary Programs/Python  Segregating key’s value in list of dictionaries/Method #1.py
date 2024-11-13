# Python3 code to demonstrate working of
# Segregating key's value in list of dictionaries
# Using generator expression

# Initialize list
test_list = [{'gfg': 1, 'best': 2}, {'gfg': 4, 'best': 5}]

# printing original list
print("The original list : " + str(test_list))

# Using generator expression
# Segregating key's value in list of dictionaries
res = [tuple(sub["gfg"] for sub in test_list),
       tuple(sub["best"] for sub in test_list)]

# printing result
print("Segregated values of keys are : " + str(res))
