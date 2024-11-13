# Python3 code to Get the number of keys
# with given value N in dictionary

# Initialize dictionary
test_dict = {'gfg': 1, 'is': 2, 'best': 3, 'for': 2, 'CS': 2}

# printing original dictionary
print("The original dictionary : " + str(test_dict))

# Initialize value
N = 2

# Using loop
# Selective key values in dictionary
res = 0
for key in test_dict:
    if test_dict[key] == N:
        res = res + 1

# printing result
print("Frequency of N is : " + str(res))
