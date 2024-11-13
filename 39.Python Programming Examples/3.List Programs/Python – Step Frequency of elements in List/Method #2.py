# Python3 code to demonstrate
# Step Frequency of elements in List
# using list comprehension + enumerate()
from collections import defaultdict

# Initializing loop
test_list = ['gfg', 'is', 'best', 'gfg', 'is', 'life']

# printing original list
print("The original list is : " + str(test_list))

# Step Frequency of elements in List
# using list comprehension + enumerate()
res = [test_list[ : idx + 1].count(ele) for (idx, ele) in enumerate(test_list)]

# printing result
print ("Step frequency of elements is : " + str(res))
