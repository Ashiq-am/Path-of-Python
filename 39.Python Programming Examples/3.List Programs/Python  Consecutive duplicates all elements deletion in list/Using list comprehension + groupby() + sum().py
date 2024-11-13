# Python3 code to demonstrate working of
# Consecutive duplicates all elements deletion in list
# using list comprehension + sum() + groupby()
from itertools import groupby

# initialize list
test_list = [1, 1, 3, 4, 4, 4, 5, 6, 6, 7, 8, 8, 6]

# printing original list
print("The original list is : " + str(test_list))

# Consecutive duplicates all elements deletion in list
# using list comprehension + sum() + groupby()
res = [i for i, j in groupby(test_list) if sum(1 for x in j) < 2]

# printing result
print("List after consecutive duplicates elements deletion : " + str(res))
