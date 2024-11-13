# Python3 code to demonstrate working of
# Total equal pairs in List
# Using Counter() + list comprehension + sum()
from collections import Counter

# initializing lists
test_list = [2, 4, 5, 2, 5, 4, 2, 4, 5, 7, 7, 8, 3]

# printing original list
print("The original list is : " + str(test_list))

# using Counter for getting elements count
res = sum(ele // 2 for ele in Counter(test_list).values())

# printing result
print("Total Pairs : " + str(res))
