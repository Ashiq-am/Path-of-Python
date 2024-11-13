# Python3 code to demonstrate working of
# Concatenate Dictionary string values
# Using Counter() + "+" operator
from collections import Counter

# Initialize dictionaries
test_dict1 = {'gfg' : 'a', 'is' : 'b', 'best' : 'c'}
test_dict2 = {'gfg' : 'd', 'is' : 'e', 'best' : 'f'}

# printing original dictionaries
print("The original dictionary 1 : " + str(test_dict1))
print("The original dictionary 2 : " + str(test_dict2))

# Using Counter() + "+" operator
# Concatenate Dictionary string values
temp1 = Counter(test_dict1)
temp2 = Counter(test_dict2)
res = Counter({key : temp1[key] + temp2[key] for key in temp1})

# printing result
print("The string concatenation of dictionary is : " + str(dict(res)))
