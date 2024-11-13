# Python3 code to demonstrate working of
# Selective Key Values Summation
# Using sum() + list comprehension

# initializing dictionary
test_dict = {'Gfg' : 4, 'is' : 2, 'best' : 7, 'for' : 9, 'geeks' : 10}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# initializing keys_list
key_list = ['Gfg', 'best', 'geeks']

# Selective Key Values Summation
# Using sum() + list comprehension
res = sum([test_dict[key] for key in key_list])

# printing result
print("The keys summation : " + str(res))
