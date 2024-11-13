# importing library

from scipy.stats import kappa3

numargs = kappa3.numargs
a, b = 4.32, 3.18
rv = kappa3(a, b)

print("RV : \n", rv)
