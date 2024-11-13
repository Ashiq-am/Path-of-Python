# Python3 code to demonstrate working of
# Subtract String Lists
# using Counter() + elements()
from collections import Counter

# initialize lists
test_list1 = ["gfg", "is", "best", "for", "CS"]
test_list2 = ["preffered", "is", "gfg"]

# printing original lists
print("The original list 1 : " + str(test_list1))
print("The original list 2 : " + str(test_list2))

# Subtract String Lists
# using Counter() + elements()
res = list((Counter(test_list1)-Counter(test_list2)).elements())

# printing result
print("The Subtracted list is : " + str(res))
