# Python3 code to demonstrate working of
# Sorted Nested Keys in Dictionary
# Using sorted() + list comprehension + isinstance()

# initializing dictionary
test_dict = {'gfg': 43, 'is': {'best': 14, 'for': 35, 'geeks': 42}, 'and': {'CS': 29}}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# Sorted Nested Keys in Dictionary
# Using sorted() + list comprehension + isinstance()
res = sorted([key for val in test_dict.values() if isinstance(val, dict)
              for key in val] + list(test_dict))

# printing result
print("The sorted nested keys : " + str(res))
