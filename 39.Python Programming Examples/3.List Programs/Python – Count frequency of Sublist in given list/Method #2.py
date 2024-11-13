# Python3 code to demonstrate working of
# Sublist Frequency
# Using zip_longest() + islice() + all() + loop
from itertools import zip_longest, islice

# initializing list
test_list = [4, 5, 3, 5, 7, 8, 3, 5, 7, 2, 7, 3, 2]

# printing original list
print("The original list is : " + str(test_list))

# initializing Sublist
sublist = [3, 5, 7]

# slicing is used to extract chunks and compare
res = []
idx = 0
while True:
    try:

        # getting to the index
        idx = test_list.index(sublist[0], idx)
    except ValueError:
        break

    # using all() to check for all elements equivalence
    if all(x == y for (x, y) in zip_longest(sublist, islice(test_list, idx, idx + len(sublist)))):
        res.append(sublist)
        idx += len(sublist)
    idx += 1

res = len(res)

# printing result
print("The sublist count : " + str(res))
