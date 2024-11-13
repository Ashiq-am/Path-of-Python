# Python code to demonstrate the error caused
# when garbage value of xbar is entered

# Importing statistics module
import statistics

# creating a sample list
sample = (1, 1.3, 1.2, 1.9, 2.5, 2.2)

# calculating the mean of sample set
m = statistics.mean(sample)

# Actual value of mean after calculation
# comes out to 1.6833333333333333
# But to demonstrate xbar error let's enter
# -100 as the value for xbar parameter
print(statistics.variance(sample, xbar = -100))
