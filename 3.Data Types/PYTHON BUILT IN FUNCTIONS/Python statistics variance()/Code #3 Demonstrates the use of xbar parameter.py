# Python code to demonstrate
# the use of xbar parameter

# Importing statistics module
import statistics

# creating a sample list
sample = (1, 1.3, 1.2, 1.9, 2.5, 2.2)

# calculating the mean of sample set
m = statistics.mean(sample)


# calculating the variance of sample set
print("Variance of Sample set is % s"
	%(statistics.variance(sample, xbar = m)))
