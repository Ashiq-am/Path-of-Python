# importing library

from scipy.stats import loglaplace

numargs = loglaplace.numargs
a, b = 4.32, 3.18
rv = loglaplace(a, b)

print("RV : \n", rv)
