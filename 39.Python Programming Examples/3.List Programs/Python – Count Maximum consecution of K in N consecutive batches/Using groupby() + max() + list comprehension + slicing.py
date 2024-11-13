# Python3 code to demonstrate working of
# Maximum consecution of K in N consecutive batches
# Using groupby() + max() + list comprehension + slicing
from itertools import groupby

# initializing list
test_list = [4, 4, 5, 4, 4, 4, 1, 2, 3, 4, 4, 4, 4, 4, 4,
             4, 5, 6, 7, 4, 4, 5, 3, 4, 4, 4, 7, 4, 4, 4,
             5, 6, 3, 5, 4, 4, 4, 6, 4, 4, 1, 4, 2, 4, 4]

# printing original list
print("The original list is : " + str(test_list))

# initializing N
N = 15

# initializing K
K = 4

# max() getting max. consecution of K, ranges being evaluated using slices
# and skips using range()
res = [max(len(list(grup)) for ele, grup in groupby(sub) if ele == K)
       for sub in (test_list[idx: idx + N]
                   for idx in range(0, len(test_list), N))]

# printing result
print("Maximum consecution of K for each batch : " + str(res))
