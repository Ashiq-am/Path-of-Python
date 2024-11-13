# Python3 code to demonstrate working of
# Closest key in dictionary
# Using list comprehension + keys() + lambda

# initializing dictionary
test_dict = {13 : 'Hi', 15 : 'Hello', 16 : 'Gfg'}

# initializing nearest key
search_key = 15.6

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# Using list comprehension + keys() + lambda
# Closest key in dictionary
res = test_dict.get(search_key) or test_dict[
	min(test_dict.keys(), key = lambda key: abs(key-search_key))]

# printing result
print("The value to the closest key : " + str(res))
