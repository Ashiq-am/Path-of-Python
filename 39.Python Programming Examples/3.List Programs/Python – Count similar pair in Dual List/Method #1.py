# Python3 code to demonstrate
# Count Similar pair in dual list
# using Counter() + map() + sorted() + items()
from collections import Counter

# initializing list
test_list = [[1, 2], [2, 1], [3, 4], [4, 3], [5, 4]]

# printing original list
print ("The original list is : " + str(test_list))

# Count Similar pair in dual list
# using Counter() + map() + sorted() + items()
temp = [sorted(ele) for ele in test_list]
res = [(i, j, k) for (i, j), k in Counter(map(tuple, temp)).items()]

# printing result
print ("The dual list similarity counts : " + str(res))
