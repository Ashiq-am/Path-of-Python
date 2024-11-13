# Python3 code to demonstrate working of
# Summation of Custom nested keys in Dictionary
# Using loop

# initializing dictionary
test_dict = {'Gfg': {1: 6, 5: 9, 9: 12},
             'is': {1: 9, 5: 7, 9: 2},
             'best': {1: 3, 5: 4, 9: 14}}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# initializing sum keys
sum_key = [1, 9]

sum = 0
for ele in sum_key:
    for key, val in test_dict.items():
        # extracting summation of required values
        sum = sum + val[ele]

# printing result
print("The required summation : " + str(sum))
