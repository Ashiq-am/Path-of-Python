# Python3 code to demonstrate working of
# Longest String in list
# using max() + key

# initialize list
test_list = ['gfg', 'is', 'best', 'for', 'geeks']

# printing original list
print("The original list : " + str(test_list))

# Longest String in list
# using max() + key
res = max(test_list, key = len)

# printing result
print("Maximum length string is : " + res)
