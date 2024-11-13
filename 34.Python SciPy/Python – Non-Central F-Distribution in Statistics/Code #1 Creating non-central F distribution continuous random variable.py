# importing library

from scipy.stats import ncf

numargs = ncf.numargs
a, b = 4.32, 3.18
rv = ncf(a, b)

print("RV : \n", rv)
