# Python3 code to demonstrate working of
# Remove digits from Dictionary String Values List
# Using loop + regex() + dictionary comprehension
import re

# initializing dictionary
test_dict = {'Gfg': ["G4G is Best 4", "4 ALL geeks"],
             'is': ["5 6 Good"],
             'best': ["Gfg Heaven", "for 7 CS"]}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# using dictionary comprehension to go through all keys
res = {key: [re.sub('\d', '', ele) for ele in val]
       for key, val in test_dict.items()}

# printing result
print("The filtered dictionary : " + str(res))
