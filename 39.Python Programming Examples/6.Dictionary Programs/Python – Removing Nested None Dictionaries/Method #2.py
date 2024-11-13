# Python3 code to demonstrate working of
# Removing Nested None Dictionaries
# Using dictionary comprehension

# initializing dictionary
test_dict = {'gfg' : {'a': 5}, 'best' : {}, 'for' : {}, 'geeks' : {'b' : 6}}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# Removing Nested None Dictionaries
# Using dictionary comprehension
res = {key : val for key, val in test_dict.items() if val}

# printing result
print("The dictionary after filtering is : " + str(res))
