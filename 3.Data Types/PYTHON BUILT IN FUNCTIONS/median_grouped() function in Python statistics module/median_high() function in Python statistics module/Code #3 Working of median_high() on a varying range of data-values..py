# Python code to demonstrate the
# working of median_high()

# importing statistics module
from statistics import median_high

# Importing fractions module as fr
from fractions import Fraction as fr

# tuple of positive integer numbers
data1 = (2, 3, 4, 5, 7, 9, 11)

# tuple of a set of floating-point values
data2 = (2.4, 5.1, 6.7, 8.9)

# tuple of a set of fractional numbers
data3 = (fr(1, 2), fr(44, 12),
		fr(10, 3), fr(2, 3))

# tuple of a set of negative integers
data4 = (-5, -1, -12, -19, -3)

# tuple of set of positive
# and negative integers
data5 = (-1, -2, -3, -4, 4, 3, 2, 1)

# Print the high_median() of the given data-sets
print("High Median of data-set 1 is %s" % (median_high(data1)))
print("High Median of data-set 2 is %s" % (median_high(data2)))
print("High Median of data-set 3 is %s" % (median_high(data3)))
print("High Median of data-set 4 is %s" % (median_high(data4)))
print("High Median of data-set 5 is %s" % (median_high(data5)))
