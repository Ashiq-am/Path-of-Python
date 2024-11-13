# Python code to demonstrate the
# statistics error in mode function

'''
StatisticsError is raised while using mode when there are
two equal modes present in a data set and when the data set
is empty or null
'''

# importing statistics module
import statistics

# creating a data set consisting of two equal data-sets
data1 = [1, 1, 1, -1, -1, -1]

# In the above data set
# Count of 1 is 3
# Count of -1 is also 3
# StatisticsError will be raised

print(statistics.mode(data1))
