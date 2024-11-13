# importing library

from scipy.stats import loggamma

numargs = loggamma.numargs
a, b = 4.32, 3.18
rv = loggamma(a, b)

print("RV : \n", rv)
