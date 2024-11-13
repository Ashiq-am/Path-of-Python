# Python3 code to demonstrate working of
# Dictionary Keys Summation
# Using keys() + sum()

# initializing dictionary
test_dict = {3: 4, 9: 10, 15: 10, 5: 7, 6: 7}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# sum() performs summation
res = sum(list(test_dict.keys()))

# printing result
print("The dictionary keys summation : " + str(res))
