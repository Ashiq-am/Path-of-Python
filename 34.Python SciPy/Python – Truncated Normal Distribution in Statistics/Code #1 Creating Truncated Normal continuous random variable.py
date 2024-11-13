# importing library

from scipy.stats import truncnorm

numargs = truncnorm.numargs
a, b = 0.2, 0.8
rv = truncnorm(a, b)

print("RV : \n", rv)
