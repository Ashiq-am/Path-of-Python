# Python3 code to demonstrate working of
# Key index in Dictionary
# Using list comprehension + enumerate()

# initializing dictionary
test_dict = {'all' : 1, 'food' : 2, 'good' : 3, 'have' : 4}

# initializing search key string
search_key = 'good'

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# Using list comprehension + enumerate()
# Key index in Dictionary
temp = list(test_dict.items())
res = [idx for idx, key in enumerate(temp) if key[0] == search_key]

# printing result
print("Index of search key is : " + str(res))
