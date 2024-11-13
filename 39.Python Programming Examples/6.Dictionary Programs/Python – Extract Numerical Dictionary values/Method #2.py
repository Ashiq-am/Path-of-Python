# Python3 code to demonstrate working of
# Extract Numerical Dictionary values
# Using list comprehension + zip() + isdigit()

# initializing dictionary
test_dict = {"Gfg": ["34", "45", 'geeks'], 'is': ["875", None, "15"], 'best': ["98", 'abc', '12k']}

# printing original dictionary
print("The original dictionary : " + str(test_dict))

# Extract Numerical Dictionary values
# Using list comprehension + zip() + isdigit()
res = [(a, b, c) for a, b, c in zip(*test_dict.values()) if a.isdigit()]

# printing result
print("The Numerical values : " + str(res))
