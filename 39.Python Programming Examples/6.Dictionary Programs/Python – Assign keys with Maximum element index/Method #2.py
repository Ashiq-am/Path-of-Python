# Python3 code to demonstrate working of
# Assign keys with Maximum element index
# Using dictionary comprehension + max() + index()

# initializing dictionary
test_dict = {"gfg": [5, 3, 6, 3], "is": [1, 7, 5, 3], "best": [9, 1, 3, 5]}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# using dictionary comprehension as one liner alternative
res = {key: test_dict[key].index(max(test_dict[key])) for key in test_dict}

# printing result
print("The maximum index assigned dictionary : " + str(res))
