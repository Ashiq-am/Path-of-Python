# Python3 code to demonstrate working of
# Keys with specific suffix in Dictionary
# Using dictionary comprehension + endswith()

# Initialize dictionary
test_dict = {'all' : 4, 'geeks' : 5, 'are' : 8, 'freaks' : 10}

# printing original dictionary
print("The original dictionary : " + str(test_dict))

# Initialize suffix
test_suf = 'ks'

# Using dictionary comprehension + endswith()
# Keys with specific suffix in Dictionary
res = {key:val for key, val in test_dict.items() if key.endswith(test_suf)}

# printing result
print("Filtered dictionary keys are : " + str(res))
