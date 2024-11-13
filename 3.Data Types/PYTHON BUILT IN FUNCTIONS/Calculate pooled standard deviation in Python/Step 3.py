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


pooled_standard_deviation = math.sqrt(((n1 - 1)*SD1 * SD1 + (n2-1)*SD2 * SD2) / (n1 + n2-2))
print("Pooled Standard Deviation = ",pooled_standard_deviation)
