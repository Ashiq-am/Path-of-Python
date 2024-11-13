# Python3 code to demonstrate working of
# Remove Keys with K value
# Using dictionary comprehension

# initializing dictionary
test_dict = {'Gfg': 6, 'is': 7, 'best': 9, 'for': 6, 'geeks': 11}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# initializing K
K = 6

# using dictionary comprehension
# to compare not equal to K and retain
res = {key: val for key, val in test_dict.items() if val != K}

# printing result
print("The filtered dictionary : " + str(res))
