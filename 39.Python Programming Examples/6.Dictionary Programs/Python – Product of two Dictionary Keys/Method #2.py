# Python3 code to demonstrate working of
# Dictionary Keys Product
# Using Counter() + "*" operator
from collections import Counter

# Initialize dictionaries
test_dict1 = {'gfg' : 6, 'is' : 4, 'best' : 7}
test_dict2 = {'gfg' : 10, 'is' : 6, 'best' : 10}

# printing original dictionaries
print("The original dictionary 1 : " + str(test_dict1))
print("The original dictionary 2 : " + str(test_dict2))

# Using Counter() + "*" operator
# Dictionary Keys Product
temp1 = Counter(test_dict1)
temp2 = Counter(test_dict2)
res = Counter({key : temp1[key] * temp2[key] for key in temp1})

# printing result
print("The product dictionary is : " + str(dict(res)))
