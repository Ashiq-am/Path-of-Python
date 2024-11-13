# importing library

from scipy.stats import weibull_min

numargs = weibull_min.numargs
a, b = 0.2, 0.8
rv = weibull_min(a, b)

print("RV : \n", rv)
