# importing library

from scipy.stats import laplace

numargs = laplace.numargs
a, b = 4.32, 3.18
rv = laplace(a, b)

print("RV : \n", rv)
