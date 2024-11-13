# importing library

from scipy.stats import logistic

numargs = logistic.numargs
a, b = 4.32, 3.18
rv = logistic(a, b)

print("RV : \n", rv)
