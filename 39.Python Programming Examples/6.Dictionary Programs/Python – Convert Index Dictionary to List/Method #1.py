# Python3 code to demonstrate working of
# Convert Index Dictionary to List
# Using list comprehension + keys()

# initializing dictionary
test_dict = { 2 : 'Gfg', 4 : 'is', 6 : 'Best' }

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# Convert Index Dictionary to List
# Using list comprehension + keys()
res = [test_dict[key] if key in test_dict.keys() else 0 for key in range(10)]

# printing result
print("The converted list : " + str(res))
