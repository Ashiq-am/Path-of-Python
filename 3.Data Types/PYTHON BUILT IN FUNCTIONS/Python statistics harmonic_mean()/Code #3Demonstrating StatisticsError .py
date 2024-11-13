# Python code to demonstrate StatisticsError
# while using harmonic_mean()

# importing statistics module
import statistics

# data-set of numbers containing
# a negative number
dat1 = [1, -1]

# Statistics Error is raised when the
# data-set passed as parameter is
# empty or contain a negative value
print(statistics.harmonic_mean(dat1))
