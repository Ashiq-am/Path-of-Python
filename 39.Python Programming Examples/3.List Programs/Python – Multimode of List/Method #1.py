# Python3 code to demonstrate working of
# Multimode of List
# using loop + formula
import math
from collections import Counter

# initialize list
test_list = [1, 2, 1, 2, 3, 4, 3]

# printing original list
print("The original list is : " + str(test_list))

# Multimode of List
# using loop + formula
res = []
test_list1 = Counter(test_list)
temp = test_list1.most_common(1)[0][1]
for ele in test_list:

    if test_list.count(ele) == temp:
        res.append(ele)


res = list(set(res))

# printing result
print("The multimode of list is : " + str(res))
