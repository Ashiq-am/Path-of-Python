# Python3 code to demonstrate working of
# Values Frequency Index List
# Using Counter() + list comprehension
from collections import Counter

# initializing list
test_list = [('Gfg', 3), ('is', 3), ('best', 1), ('for', 5), ('geeks', 1)]

# printing original list
print("The original list is : " + str(test_list))

# Values Frequency Index List
# Using Counter() + list comprehension
cntr = Counter(ele[1] for ele in test_list)
res = [cntr[idx] for idx in range(6)]

# printing result
print("The Frequency list : " + str(res))
