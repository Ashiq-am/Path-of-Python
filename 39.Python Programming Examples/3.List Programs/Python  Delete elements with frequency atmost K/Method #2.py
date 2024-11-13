# Python3 code to demonstrate
# remove elements less than and equal K
# using Counter() + list comprehension
from collections import Counter

# initializing list
test_list = [1, 4, 3, 2, 3, 3, 2, 2, 2, 1]

# printing original list
print("The original list : " + str(test_list))

# initializing K
K = 2

# using Counter() + list comprehension
# remove elements less than K
freq = Counter(test_list)
res = [ele for ele in test_list if freq[ele] > K]

# print result
print("The list removing elements less than and equal K : " + str(res))
