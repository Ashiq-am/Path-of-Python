# Python3 code to demonstrate working of
# Remove Disjoint Tuple keys from Dictionary
# Using set() + dictionary comprehension + isdisjoint()

# initializing dictionary
test_dict = {('Gfg', 3) : 4, ('is', 6) : 2, ('best', 10) : 3, ('for', 9) : 'geeks'}

# printing original dictionary
print("The original dictionary : " + str(test_dict))

# initializing List
rem_list = [9, 'is']

# Remove Disjoint Tuple keys from Dictionary
# Using set() + dictionary comprehension + isdisjoint()
res = {keys: val for keys, val in test_dict.items() if set(keys).isdisjoint(rem_list)}

# printing result
print("Dictionary after removal : " + str(res))
