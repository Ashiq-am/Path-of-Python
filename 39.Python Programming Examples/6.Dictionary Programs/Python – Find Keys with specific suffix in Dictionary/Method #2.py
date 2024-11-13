# Python3 code to demonstrate working of
# Keys with specific suffix in Dictionary
# Using map() + filter() + items() + endswith()

# Initialize dictionary
test_dict = {'all' : 4, 'geeks' : 5, 'are' : 8, 'freaks' : 10}

# printing original dictionary
print("The original dictionary : " + str(test_dict))

# Initialize suffix
test_suf = 'ks'

# Using map() + filter() + items() + endswith()
# Keys with specific suffix in Dictionary
res = dict(filter(lambda item: item[0].endswith(test_suf), test_dict.items()))

# printing result
print("Filtered dictionary keys are : " + str(res))
