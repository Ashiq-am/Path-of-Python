# Python3 code to demonstrate working of
# Symmetric Difference of Multiple sets
# Using Counter() + chain.from_iterable()
from collections import Counter
from itertools import chain

# initializing list
test_list = [{5, 3, 2, 6, 1},
             {7, 5, 3, 8, 2},
             {9, 3},
             {0, 3, 6, 7}]

# printing original list
print("The original list is : " + str(test_list))

# getting frequencies using Counter()
# from_iterable() flattens the list
freq = Counter(chain.from_iterable(test_list))

# getting frequency count 1
res = {idx for idx in freq if freq[idx] == 1}

# printing result
print("Symmetric difference of multiple list : " + str(res))
