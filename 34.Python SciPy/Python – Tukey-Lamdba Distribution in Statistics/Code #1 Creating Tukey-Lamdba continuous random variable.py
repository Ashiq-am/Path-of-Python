# importing library

from scipy.stats import tukeylambda

numargs = tukeylambda.numargs
a, b = 0.2, 0.8
rv = tukeylambda(a, b)

print("RV : \n", rv)
