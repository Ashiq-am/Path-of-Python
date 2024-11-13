# Python3 code to demonstrate working of
# Verticle Grouping Value Lists
# Using list comprehension + zip() + * operator

# initializing dictionary
test_dict = {'Gfg': [4, 5, 7], 'is': [8, 9, 10], 'best': [10, 12, 14]}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# Vertical Grouping Value Lists
# Using list comprehension + zip() + * operator
res = [tuple(idx) for idx in zip(*test_dict.values())]

# printing result
print("The grouped values : " + str(res))
