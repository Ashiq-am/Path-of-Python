# Python3 code to demonstrate working of
# Mathematical Median of Cumulative Records
# Using chain() + statistics.median()
import statistics
from itertools import chain

# initializing list
test_list = [(1, 4, 5), (7, 8), (2, 4, 10)]

# printing list
print("The original list : " + str(test_list))

# Mathematical Median of Cumulative Records
# Using chain() + statistics.median()
temp = list(chain(*test_list))
res = statistics.median(temp)

# Printing result
print("Median of Records is : " + str(res))
