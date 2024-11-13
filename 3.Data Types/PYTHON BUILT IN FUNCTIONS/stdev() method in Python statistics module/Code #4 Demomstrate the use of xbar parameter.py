# Python code to demonstrate use of xbar
# parameter while using stdev() function

# Importing statistics module
import statistics

# creating a sample list
sample = (1, 1.3, 1.2, 1.9, 2.5, 2.2)

# calculating the mean of sample set
m = statistics.mean(sample)

# xbar is nothing but stores
# the mean of the sample set

# calculating the variance of sample set
print("Standard Deviation of Sample set is % s"
		%(statistics.stdev(sample, xbar = m)))
