# Python3 code to demonstrate working of
# Check if any String is empty in list
# using in operator

# initialize list
test_list = ['gfg', 'is', 'best', '', 'for', 'geeks']

# printing original list
print("The original list : " + str(test_list))

# Check if any String is empty in list
# using in operator
res = '' in test_list

# printing result
print("Is any string empty in list? : " + str(res))
