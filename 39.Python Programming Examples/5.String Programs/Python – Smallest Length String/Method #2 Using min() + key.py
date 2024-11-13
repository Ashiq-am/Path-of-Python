# Python3 code to demonstrate working of
# Smallest Length String
# using min() + key

# initialize list
test_list = ['gfg', 'is', 'best', 'for', 'geeks']

# printing original list
print("The original list : " + str(test_list))

# Smallest Length String
# using min() + key
res = min(test_list, key = len)

# printing result
print("Minimum length string is : " + res)
