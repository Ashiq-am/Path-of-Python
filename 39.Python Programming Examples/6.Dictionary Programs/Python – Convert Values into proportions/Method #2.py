# Python3 code to demonstrate working of
# Convert Values into proportions
# Using dictionary comprehension + sum()

# initializing dictionary
test_dict = { 'gfg' : 10, 'is' : 15, 'best' : 20 }

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# Convert Values into proportions
# Using dictionary comprehension + sum()
temp = sum(test_dict.values())
res = {key: val / temp for key, val in test_dict.items()}

# printing result
print("The proportions divided values : " + str(res))
