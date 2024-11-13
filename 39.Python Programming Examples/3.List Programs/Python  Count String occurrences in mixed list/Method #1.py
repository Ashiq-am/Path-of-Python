# Python3 code to demonstrate working of
# Check String occurrences in mixed list
# using isinstance() + list comprehension

# initialize list
test_list = ['gfg', 1, True, 'is', 2, 'best']

# printing original list
print("The original list : " + str(test_list))

# Check String occurrences in mixed list
# using isinstance() + list comprehension
res = len([val for val in test_list if isinstance(val, str)])

# printing result
print("Number of strings in list : " + str(res))
