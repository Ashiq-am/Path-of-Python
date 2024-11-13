# Python3 code to demonstrate working of
# Keys with shortest length lists in dictionary
# Using list comprehension

# initializing dictionary
test_dict = {'gfg': [4, 5],
             'is': [9, 7, 3, 10],
             'best': [11, 34],
             'for': [6, 8, 2],
             'geeks': [12, 24]}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# Keys with shortest length lists in dictionary
# Using list comprehension
min_val = min([len(test_dict[ele]) for ele in test_dict])
res = [key for key, val in test_dict.items() if len(val) == min_val]

# printing result
print("The required keys are : " + str(res))
