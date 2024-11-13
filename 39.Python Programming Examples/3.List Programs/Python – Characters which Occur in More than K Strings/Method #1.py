# Python3 code to demonstrate
# Characters which Occur in More than K Strings
# using set() + Counter() + loop + items()
from collections import Counter
from itertools import chain


def char_ex(strs, k):
    temp = (set(sub) for sub in strs)
    counts = Counter(chain.from_iterable(temp))
    return {chr for chr, count in counts.items() if count >= k}


# Initializing list
test_list = ['Gfg', 'ise', 'for', 'Geeks']

# printing original list
print("The original list is : " + str(test_list))

# Initializing K
K = 2

# Characters which Occur in More than K Strings
# using set() + Counter() + loop + items()
res = char_ex(test_list, K)

# printing result
print("Filtered Characters are : " + str(res))
