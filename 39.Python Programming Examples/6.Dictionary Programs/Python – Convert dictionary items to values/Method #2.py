# Python3 code to demonstrate working of
# Convert dictionary items to values
# Using list comprehension

# initializing dictionary
test_dict = {'Gfg': 1, 'is': 2, 'best': 3}

# printing original dictionary
print("The original dictionary : " + str(test_dict))

# Convert dictionary items to values
# Using list comprehension
res = [{'key': key, 'value': test_dict[key]} for key in test_dict]

# printing result
print("Converted Dictionary : " + str(res))
