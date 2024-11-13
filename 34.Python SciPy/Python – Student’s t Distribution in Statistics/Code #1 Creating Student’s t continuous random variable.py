# importing library

from scipy.stats import t

numargs = t.numargs
a, b = 4.32, 3.18
rv = t(a, b)

print("RV : \n", rv)
