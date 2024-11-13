# stats.trim1() method
import numpy as np
from scipy import stats

arr1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print ("\narr1 : ", arr1)

print ("\nclipped arr1 : \n",
	stats.trim1(arr1, proportiontocut = .3, tail = 'right'))

print ("\nclipped arr1 : \n",
	stats.trim1(arr1, proportiontocut = .3, tail = 'left'))

print ("\nclipped arr1 : \n",
	stats.trim1(arr1, proportiontocut = .1, tail = 'left'))

print ("\nclipped arr1 : \n",
	stats.trim1(arr1, proportiontocut = .1, tail = 'right'))
