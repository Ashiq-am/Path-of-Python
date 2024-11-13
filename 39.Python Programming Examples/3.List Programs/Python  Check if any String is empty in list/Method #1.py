# Python3 code to demonstrate working of
# Check if any String is empty in list
# using len() + any()

# initialize list
test_list = ['gfg', 'is', 'best', '', 'for', 'geeks']

# printing original list
print("The original list : " + str(test_list))

# Check if any String is empty in list
# using len() + any()
res = any(len(ele) == 0 for ele in test_list)

# printing result
print("Is any string empty in list? : " + str(res))
