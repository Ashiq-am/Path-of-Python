# Python3 code to demonstrate working of
# Sort dictionary by value list length
# using sorted() + join() + lambda

# Initialize dictionary
test_dict = {'is' : [1, 2], 'gfg' : [3], 'best' : [1, 3, 4]}

# Printing original dictionary
print("The original dictionary is : " + str(test_dict))

# using sorted() + join() + lambda
# Sort dictionary by value list length
res = ' '.join(sorted(test_dict, key = lambda key: len(test_dict[key])))

# printing result
print("Sorted keys by value list : " + res)
