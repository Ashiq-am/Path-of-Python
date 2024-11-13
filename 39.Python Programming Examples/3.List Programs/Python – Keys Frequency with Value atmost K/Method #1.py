# Python3 code to demonstrate working of
# Keys Frequency with Value atmost K
# Using loop

# Initialize dictionary
test_dict = {'gfg': 1, 'is': 2, 'best': 3, 'for': 4, 'CS': 5}

# printing original dictionary
print("The original dictionary : " + str(test_dict))

# Initialize value
K = 3

# Using loop
# Keys Frequency with Value atmost K
res = 0
for key in test_dict:
    if test_dict[key] <= K:
        res = res + 1

# printing result
print("Frequency of keys with values till K is : " + str(res))
