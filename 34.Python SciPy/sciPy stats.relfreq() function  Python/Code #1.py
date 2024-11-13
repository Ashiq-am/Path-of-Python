# relative frequency
from scipy import stats
import numpy as np

arr1 = [1, 3, 27, 2, 5, 13]
print ("Array element : ", arr1, "\n")

a, b, c, d = stats.relfreq(arr1, numbins = 4)

print ("cumulative frequency : ", a)
print ("Lower Limit : ", b)
print ("bin size : ", c)
print ("extra-points : ", d)
