# Python3 code to demonstrate working of
# Extract Item with Maximum Tuple Value
# Using max() + lambda

# initializing dictionary
test_dict = {'gfg': (4, 6),
             'is': (7, 8),
             'best': (8, 2)}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# initializing tuple index
# 0 based indexing
tup_idx = 1

# Extract Item with Maximum Tuple Value
# Using max() + lambda
res = max(test_dict.items(), key=lambda ele: ele[1][tup_idx])

# printing result
print("The extracted maximum element item : " + str(res))
