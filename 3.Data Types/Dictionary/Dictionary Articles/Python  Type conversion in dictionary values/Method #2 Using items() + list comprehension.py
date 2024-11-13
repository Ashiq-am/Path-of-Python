# Python3 code to demonstrate
# Type conversion in list of dicts.
# using items() + list comprehension

# initializing list of dictionary
test_list = [{'a': '1', 'b': '2'}, {'c': '3', 'd': '4'}]

# printing original list
print("The original list is : " + str(test_list))

# using items() + list comprehension
# type converstion in list of dicts.
res = [dict([key, int(value)]
            for key, value in dicts.items())
       for dicts in test_list]

# printing result
print("The modified converted list is : " + str(res))
