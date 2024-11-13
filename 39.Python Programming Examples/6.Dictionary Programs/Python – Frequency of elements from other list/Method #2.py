# Python3 code to demonstrate working of
# Frequency of elements from other list
# Using Counter() + setdefault() + loop
from collections import Counter

# initializing lists
test_list1 = [4, 6, 8, 9, 10]
test_list2 = [4, 6, 6, 5, 8, 10, 4, 9, 8, 10, 1]

# printing original lists
print("The original list 1 : " + str(test_list1))
print("The original list 2 : " + str(test_list2))

# Counter() used to perform count on list 2
res = dict(Counter(test_list2))

# filtering only list 1 keys
res = {key: val for key, val in res.items() if key in test_list1}

for key in test_list1:
    # initializing elements not present in list 2 of list 1 to 0
    res.setdefault(key, 0)

# printing result
print("Lists elements Frequency : " + str(res))
