# importing library

from scipy.stats import kappa4

numargs = kappa4.numargs
a, b = 4.32, 3.18
rv = kappa4(a, b)

print("RV : \n", rv)
