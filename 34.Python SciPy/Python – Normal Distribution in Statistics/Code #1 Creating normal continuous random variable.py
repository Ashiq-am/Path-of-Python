# importing library

from scipy.stats import norm

numargs = norm.numargs
a, b = 4.32, 3.18
rv = norm(a, b)

print("RV : \n", rv)
