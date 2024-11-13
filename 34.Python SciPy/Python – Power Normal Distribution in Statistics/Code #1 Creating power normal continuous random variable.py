# importing library

from scipy.stats import powernorm

numargs = powernorm.numargs
a, b = 4.32, 3.18
rv = powernorm(a, b)

print("RV : \n", rv)
