# Python3 code to demonstrate working of
# Split flatten String List
# Using split() + join()

# initializing list
test_list = ['gfg-is-best', 'for-all', 'geeks-and', 'CS']

# printing original list
print("The original list is : " + str(test_list))

# Split flatten String List
# Using split() + join()
res = '-'.join(test_list).split('-')

# printing result
print("The String List after extension : " + str(res))
