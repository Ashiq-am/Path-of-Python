# Python3 code to demonstrate
# group summation of tuple list
# using Counter() + "+" operator
from collections import Counter

# initializing list of tuples
test_list1 = [('key1', 4), ('key3', 6), ('key2', 8)]
test_list2 = [('key2', 1), ('key1', 4), ('key3', 2)]

# printing original lists
print("The original list 1 : " + str(test_list1))
print("The original list 2 : " + str(test_list2))

# using Counter() + "+" operator
# group summation of tuple list
cumul_1 = Counter(dict(test_list1))
cumul_2 = Counter(dict(test_list2))
cumul_3 = cumul_1 + cumul_2
res = list(cumul_3.items())

# print result
print("The grouped summation tuple list is : " + str(res))
