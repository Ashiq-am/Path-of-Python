# Python code to demonstarte StatisticsError

# importing the statistics module
import statistics

# creating a data-set with one element
sample = [1]

# will raise StatisticsError
print(statistics.stdev(sample))
