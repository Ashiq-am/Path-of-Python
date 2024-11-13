# importing library

from scipy.stats import poisson

numargs = poisson.numargs
a, b = 0.2, 0.8
rv = poisson(a, b)

print("RV : \n", rv)
