# importing library

from scipy.stats import lomax

numargs = lomax.numargs
a, b = 4.32, 3.18
rv = lomax(a, b)

print("RV : \n", rv)
