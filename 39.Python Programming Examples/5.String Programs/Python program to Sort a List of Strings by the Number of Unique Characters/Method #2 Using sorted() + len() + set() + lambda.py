# Python3 code to demonstrate working of
# Sort Strings by Unique characters
# Using sorted() + len() + set() + lambda

# initializing list
test_list = ['gfg', 'best', 'for', 'geeks']

# printing original list
print("The original list is : " + str(test_list))

# perform sort
res = sorted(test_list, key=lambda sub: len(list(set(sub))))

# printing result
print("Sorted List : " + str(res))
