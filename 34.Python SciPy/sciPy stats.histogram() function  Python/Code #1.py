# building the histogram
import scipy
import numpy as np
import matplotlib.pyplot as plt

hist, bin_edges = scipy.histogram([1, 1, 2, 2, 2, 2, 3],
									bins = range(5))

# Checking the results
print ("No. of points in each bin : ", hist)
print ("Size of the bins		 : ", bin_edges)

# plotting the histogram
plt.bar(bin_edges[:-1], hist, width = 1)
plt.xlim(min(bin_edges), max(bin_edges))
plt.show()
