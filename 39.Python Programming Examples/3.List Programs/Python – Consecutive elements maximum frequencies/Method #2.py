# Python3 code to demonstrate working of
# Consecutive elements maximum frequencies
# Using max() + list comprehension + set() + groupby()
from itertools import groupby

# initializing list
test_list = [5, 6, 7, 7, 6, 6, 5, 7]

# printing original list
print("The original list is : " + str(test_list))

# Consecutive elements maximum frequencies
# Using max() + list comprehension + set() + groupby()
temp = list(set(test_list))
res = [{ele : max([len(list(val)) for key, val in groupby(test_list)
								if ele == key])} for ele in temp]

# printing result
print("The maximum frequencies : " + str(res))
