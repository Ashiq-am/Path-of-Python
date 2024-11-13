# Python code to demonstrate the
# working of median_low()

# importing the statistics module
import statistics

# simple list of a set of integers
set1 = [1, 3, 3, 4, 5, 7]

# Print median of the data-set

# Median value may or may not
# lie within the data-set
print("Median of the set is % s"
	% (statistics.median(set1)))

# Print low median of the data-set
print("Low Median of the set is % s "
	% (statistics.median_low(set1)))
