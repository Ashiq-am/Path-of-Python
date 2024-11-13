# importing library

from scipy.stats import lognorm

numargs = lognorm.numargs
a, b = 4.32, 3.18
rv = lognorm(a, b)

print("RV : \n", rv)
