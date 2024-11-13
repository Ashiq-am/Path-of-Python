# Python3 code to demonstrate working of
# Custom order dictionary
# Using dictionary comprehension

# initializing dictionary
test_dict = {'is' : 2, 'for' : 4, 'gfg' : 1, 'best' : 3, 'geeks' : 5}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# initializing order
ord_list = ['gfg', 'is', 'best', 'for', 'geeks']

# Custom order dictionary
# Using dictionary comprehension
res = {key : test_dict[key] for key in ord_list}

# printing result
print("Ordered dictionary is : " + str(res))
