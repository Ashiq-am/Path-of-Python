# Python3 code to demonstrate
# Pairs with multiple similar values in dictionary
# using list comprehension + Counter()
from collections import Counter

# Initializing list
test_list = [{'Gfg' : 1, 'is' : 2}, {'Gfg' : 2, 'is' : 2}, {'Gfg' : 1, 'is' : 2}]

# printing original list
print("The original list is : " + str(test_list))

# Pairs with multiple similar values in dictionary
# using list comprehension + Counter()
temp = Counter(sub['Gfg'] for sub in test_list)
res = [ele for ele in test_list if temp[ele['Gfg']] > 1]

# printing result
print ("List after keeping dictionary with same key's value : " + str(res))
