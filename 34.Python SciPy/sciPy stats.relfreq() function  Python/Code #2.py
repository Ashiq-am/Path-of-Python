# relative frequency
from scipy import stats
import numpy as np

arr1 = [1, 3, 27, 2, 5, 13]
print ("Array element : ", arr1, "\n")

a, b, c, d = stats.relfreq(arr1, numbins = 4,
			weights = [.1, .2, .1, .3, 1, 6])

print ("cumfreqs : ", a)
print ("lowlim : ", b)
print ("binsize : ", c)
print ("extrapoints : ", d)
