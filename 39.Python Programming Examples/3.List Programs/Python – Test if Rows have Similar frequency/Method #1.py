# Python3 code to demonstrate working of
# Test if Rows have Similar frequency
# Using Counter() + list comprehension
from collections import Counter

# initializing list
test_list = [[6, 4, 2, 7, 3], [7, 3, 6, 4, 2], [2, 4, 7, 3, 6]]

# printing original list
print("The original list is : " + str(test_list))

# checking if all rows are similar
res = all(dict(Counter(row)) == dict(Counter(test_list[0])) for row in test_list)

# printing result
print("Are all rows similar : " + str(res))
