# importing library

from scipy.stats import semicircular

numargs = semicircular.numargs
a, b = 4.32, 3.18
rv = semicircular(a, b)

print("RV : \n", rv)
