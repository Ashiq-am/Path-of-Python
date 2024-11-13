# Python3 code to demonstrate working of
# Convert Value list elements to List records
# Using dictionary comprehension + items()

# initializing dictionary
test_dict = {'gfg' : [4, 5], 'is' : [8], 'best' : [10]}

# printing original dictionary
print("The original dictionary : " + str(test_dict))

# Convert Value list elements to List records
# Using dictionary comprehension + items()
res = {key: [{val: []} for val in sub] for key, sub in test_dict.items()}

# printing result
print("The converted dictionary is : " + str(res))
