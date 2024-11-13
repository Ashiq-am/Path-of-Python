# importing library

from scipy.stats import weibull_max

numargs = weibull_max.numargs
a, b = 0.2, 0.8
rv = weibull_max(a, b)

print("RV : \n", rv)
