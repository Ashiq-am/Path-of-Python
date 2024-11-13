# Python3 code to demonstrate working of
# Initializing dictionary with list index-values
# Using dictionary comprehension + len()

# initializing list
test_list = ['Gfg', 'is', 'best']

# printing original list
print("The original list is : " + str(test_list))

# Initializing dictionary with list index-values
# Using dictionary comprehension + len()
res = {x : test_list[x] for x in range(len(test_list))}

# printing result
print("The dictionary indexed as list is : " + str(res))
