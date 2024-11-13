# Python3 code to demonstrate working of
# Round Off Dictionary Values to K decimals
# Using dictionary comprehension + round()

# initializing dictionary
test_dict = {"Gfg" : 54.684034, "is" : 76.324334, "Best" : 28.43524}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# initializing K
K = 3

# Encapsulating solution using single comprehension
res = {key : round(test_dict[key], K) for key in test_dict}

# printing result
print("Values after round off : " + str(res))
