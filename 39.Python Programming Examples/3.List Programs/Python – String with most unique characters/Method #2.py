# Python3 code to demonstrate
# String with most unique characters
# using max() + key + lambda

# Initializing list
test_list = ['gfg', 'is', 'best', 'for', 'geeksc']

# printing original list
print("The original list is : " + str(test_list))

# String with most unique characters
# using max() + key + lambda
res = max(test_list, key = lambda sub: len(set(sub)), default = None)

# printing result
print ("The string with most unique characters is : " + str(res))
