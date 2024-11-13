# importing library

from scipy.stats import powerlognorm

numargs = powerlognorm.numargs
a, b = 4.32, 3.18
rv = powerlognorm(a, b)

print("RV : \n", rv)
