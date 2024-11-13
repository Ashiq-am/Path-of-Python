# Python3 code to demonstrate working of
# Sort Matrix by Row Median
# Using sorted() + lambda + median()
from statistics import median

# initializing list
test_list = [[3, 4, 7], [1, 7, 2], [10, 2, 4], [8, 6, 5]]

# printing original list
print("The original list is : " + str(test_list))

# inplace sorting using sort()
res = sorted(test_list, key = lambda row : median(row))

# printing result
print("Sorted Matrix : " + str(res))
