# Python3 code to demonstrate working of
# Value list mean
# Using dictionary comprehension

# initializing dictionary
test_dict = {'Gfg' : [6, 7, 5, 4], 'is' : [10, 11, 2, 1], 'best' : [12, 1, 2]}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# Value list mean
# Using dictionary comprehension
res = {key: sum(val) / len(val) for key, val, in test_dict.items()}

# printing result
print("The dictionary average is : " + str(res))
