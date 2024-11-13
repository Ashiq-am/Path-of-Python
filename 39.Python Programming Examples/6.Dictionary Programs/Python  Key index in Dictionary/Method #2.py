# Python3 code to demonstrate working of
# Key index in Dictionary
# Using list() + keys() + index()

# initializing dictionary
test_dict = {'all' : 1, 'food' : 2, 'good' : 3, 'have' : 4}

# initializing search key string
search_key = 'good'

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# Using list() + keys() + index()
# Key index in Dictionary
res = list(test_dict.keys()).index(search_key)

# printing result
print("Index of search key is : " + str(res))
