# importing library

from scipy.stats import skellam

numargs = skellam.numargs
a, b = 0.2, 0.8
rv = skellam(a, b)

print("RV : \n", rv)
