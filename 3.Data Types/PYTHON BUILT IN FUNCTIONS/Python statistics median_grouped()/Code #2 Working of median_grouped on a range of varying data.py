# Python code to demonsrate the
# working of median_grouped()

# importing statistics module
from statistics import median_grouped

# tuple of a set of positive integers
set1 = [2, 5, 3, 4, 8, 9]

# tuple of a set of negative integers
set2 = [-6, -2, -9, -12]

# tuple of a set of positive
# and negative integers
set3 = [2, 4, 8, 9, -2, -3, -5, -6]

# Printing grouped median for
# the given set of data
print("Grouped Median of set 1 is % s" % (median_grouped(set1)))
print("Grouped Median of set 2 is % s" % (median_grouped(set2)))
print("Grouped Median of set 3 is % s" % (median_grouped(set3)))
