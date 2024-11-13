import math
import statistics
sample1 = [4, 5, 6]

# Computing sample standard deviation for sample1
SD1 = statistics.stdev(sample1)
sample2 = [10, 12, 14, 16, 18, 20]

# Computing sample standard deviation for sample2
SD2 = statistics.stdev(sample2)

# calculate length of 1st sample
n1 = len(sample1)

# calculate length of 2nd sample
n2 = len(sample2)

print("sample1 : length = ", n1, " | S.D. = ", SD1)
print("sample2 : length = ", n2, " | S.D. = ", SD2)
