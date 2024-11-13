# importing library

from scipy.stats import wrapcauchy

numargs = wrapcauchy.numargs
a, b = 0.2, 0.8
rv = wrapcauchy(a, b)

print("RV : \n", rv)
