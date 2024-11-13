# Python3 code to demonstrate working of
# Sort Matrix by Row Median
# Using sort() + median()
from statistics import median


def med_comp(row):
    # computing median
    return median(row)


# initializing list
test_list = [[3, 4, 7], [1, 7, 2], [10, 2, 4], [8, 6, 5]]

# printing original list
print("The original list is : " + str(test_list))

# inplace sorting using sort()
test_list.sort(key=med_comp)

# printing result
print("Sorted Matrix : " + str(test_list))
