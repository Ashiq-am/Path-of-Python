# Python3 code to demonstrate working of
# K modulo on each Dictionary Key
# Using update() + dictionary comprehension

# Initialize dictionary
test_dict = {'gfg' : 6, 'is' : 4, 'best' : 7}

# printing original dictionary
print("The original dictionary : " + str(test_dict))

# initializing K
K = 4

# Using update() + dictionary comprehension
# K modulo on each Dictionary Key
test_dict.update((x, y % K) for x, y in test_dict.items())

# printing result
print("The dictionary after mod K each key's value : " + str(test_dict))
