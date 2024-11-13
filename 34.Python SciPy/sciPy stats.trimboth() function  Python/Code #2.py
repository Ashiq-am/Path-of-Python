# stats.trimboth() method
import numpy as np
from scipy import stats


arr1 = [[0, 12, 21, 3, 14],
		[53, 16, 37, 85, 39]]

print ("\narr1 : ", arr1)

print ("\nclipped arr1 : \n",
	stats.trimboth(arr1, proportiontocut = .3))

print ("\nclipped arr1 : \n",
	stats.trimboth(arr1, proportiontocut = .1))

print ("\nclipped arr1 : \n",
	stats.trimboth(arr1, proportiontocut = .1, axis = 1))

print ("\nclipped arr1 : \n",
	stats.trimboth(arr1, proportiontocut = .1, axis = 0))
