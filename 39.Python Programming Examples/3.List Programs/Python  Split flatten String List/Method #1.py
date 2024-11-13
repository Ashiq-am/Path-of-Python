# Python3 code to demonstrate working of
# Split flatten String List
# Using list comprehension + split() + extend()

# initializing list
test_list = ['gfg-is-best', 'for-all', 'geeks-and', 'CS']

# printing original list
print("The original list is : " + str(test_list))

# Split flatten String List
# Using list comprehension + split() + extend()
res = []
[res.extend(idx.split("-")) for idx in test_list]

# printing result
print("The String List after extension : " + str(res))
