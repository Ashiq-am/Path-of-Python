# Python3 code to demonstrate working of
# Removing Nested None Dictionaries
# Using filter() + dict()

# initializing dictionary
test_dict = {'gfg' : {'a': 5}, 'best' : {}, 'for' : {}, 'geeks' : {'b' : 6}}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# Removing Nested None Dictionaries
# Using filter() + dict()
res = dict(filter(lambda sub: sub[1], test_dict.items()))

# printing result
print("The dictionary after filtering is : " + str(res))
