# Python code to demonstrate the
# working of median_low()

# importing the statistics module
import statistics

# simple list of a set of integers
set1 = [1, 3, 3, 4, 5, 7]

# Note: low median will always be
#	 a member of the data-set.

# Print low median of the data-set
print("Low median of the data-set is % s "
		% (statistics.median_low(set1)))
