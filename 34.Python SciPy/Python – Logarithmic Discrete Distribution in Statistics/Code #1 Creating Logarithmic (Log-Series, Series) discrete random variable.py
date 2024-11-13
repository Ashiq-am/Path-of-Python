# importing library

from scipy.stats import logser

numargs = logser.numargs
a, b = 0.2, 0.8
rv = logser(a, b)

print("RV : \n", rv)
