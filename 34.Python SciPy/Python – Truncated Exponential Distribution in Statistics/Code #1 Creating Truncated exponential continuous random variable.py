# importing library

from scipy.stats import truncexpon

numargs = truncexpon.numargs
a, b = 0.2, 0.8
rv = truncexpon(a, b)

print("RV : \n", rv)
