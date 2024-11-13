# Python code to demonstrate difference
# in results of stdev() and variance()

# importing Statistics module
import statistics

# creating a simple data-set
sample = [1, 2, 3, 4, 5]

# Printing standard deviation
# xbar is set to default value of 1
print("Standard Deviation of the sample is % s "
					%(statistics.stdev(sample)))

# variance is approximately the
# squared result of what stdev is
print("Variance of the sample is % s"
	%(statistics.variance(sample)))
