# Python3 code to demonstrate
# Elements frequency count in multiple lists
# using map() + Counter() + dictionary comprehension
from collections import Counter

# Initializing lists
test_list1 = [1, 3, 2, 4, 5, 1, 2]
test_list2 = [4, 1, 4, 3, 4, 2, 4]
test_list3 = [1, 4, 5, 3, 4, 5, 4]

# printing original lists
print("The original list 1 is : " + str(test_list1))
print("The original list 2 is : " + str(test_list2))
print("The original list 3 is : " + str(test_list3))

# Elements frequency count in multiple lists
# using map() + Counter() + dictionary comprehension
freq = list(map(Counter, (test_list1, test_list2, test_list3)))
res = {ele: [cnt[ele] for cnt in freq] for ele in {ele for cnt in freq for ele in cnt}}

# printing result
print("The frequency of each element is : " + str(res))
