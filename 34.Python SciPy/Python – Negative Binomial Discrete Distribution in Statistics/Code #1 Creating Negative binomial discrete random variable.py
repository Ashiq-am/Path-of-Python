# importing library

from scipy.stats import nbinom

numargs = nbinom.numargs
a, b = 0.2, 0.8
rv = nbinom(a, b)

print("RV : \n", rv)
