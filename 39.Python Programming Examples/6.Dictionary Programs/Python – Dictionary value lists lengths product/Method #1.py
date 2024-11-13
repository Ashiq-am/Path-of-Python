# Python3 code to demonstrate working of
# Dictionary value lists lengths product
# Using loop + len()

# initializing dictionary
test_dict = {'Gfg': [6, 5, 9, 3, 10],
             'is': [1, 3, 4],
             'best': [9, 16]}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# using loop to iterate through all keys
res = 1
for key in test_dict:
    # len() used to get length of each value list
    res = res * len(test_dict[key])

# printing result
print("The computed product : " + str(res))
