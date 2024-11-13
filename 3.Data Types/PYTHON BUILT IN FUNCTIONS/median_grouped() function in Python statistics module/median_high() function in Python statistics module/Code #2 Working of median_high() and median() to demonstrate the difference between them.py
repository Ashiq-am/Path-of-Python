# Working of median_high() and median() to
# demonstrate the difference between them.

# importing the statistics module
import statistics

# simple list of a set of integers
set1 = [1, 3, 3, 4, 5, 7]

# Print median of the data-set

# Median value may or may not
# lie within the data-set
print("Median of the set is %s"
	% (statistics.median(set1)))

# Print high median of the data-set
print("High Median of the set is %s "
	% (statistics.median_high(set1)))
