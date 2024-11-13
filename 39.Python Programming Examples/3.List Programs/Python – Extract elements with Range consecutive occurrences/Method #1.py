# Python3 code to demonstrate working of
# Extract elements with Range consecutive occurrences
# using groupby() + list comprehension
from itertools import groupby

# initialize list
test_list = [1, 1, 4, 5, 5, 6, 7, 7, 7, 8, 8, 8, 8]

# printing original list
print("The original list : " + str(test_list))

# initialize strt, end
strt, end = 2, 3

# Extract elements with Range consecutive occurrences
# using groupby() + list comprehension
res1 = [i for i, j in groupby(test_list) if len(list(j)) <= end]
res2 = [i for i, j in groupby(test_list) if len(list(j)) >= strt]
res = list(set(res1) & set(res2))

# printing result
print("The range consecutive elements are : " + str(res))
