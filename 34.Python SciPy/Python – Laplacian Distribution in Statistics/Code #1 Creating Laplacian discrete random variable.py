# importing library

from scipy.stats import dlaplace

numargs = dlaplace.numargs
a, b = 0.2, 0.8
rv = dlaplace(a, b)

print("RV : \n", rv)
