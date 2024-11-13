# Python3 code to demonstrate working of
# Extract Equal Pair Dictionary
# Using dictionary comprehension

# initializing dictionary
test_dict = { (1, 1) : 4, (2, 3) : 6, (3, 3) : 7, (5, 2) : 10, (2, 2) : 11}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# Extract Equal Pair Dictionary
# Using dictionary comprehension
res = {idx[0] : j for idx, j in test_dict.items() if idx[0] == idx[1]}

# printing result
print("The dictionary after equality testing : " + str(res))
