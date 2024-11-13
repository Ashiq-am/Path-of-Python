# Python3 code to demonstrate working of
# Sort by Rear Character in Strings List
# Using sorted() + lambda

# initializing list
test_list = ['gfg', 'is', 'best', 'for', 'geeks']

# printing original list
print("The original list is : " + str(test_list))

# lambda function for rear element
# performs non-inplace sort
res = sorted(test_list, key = lambda sub : sub[-1])

# printing result
print("Sorted List : " + str(res))
