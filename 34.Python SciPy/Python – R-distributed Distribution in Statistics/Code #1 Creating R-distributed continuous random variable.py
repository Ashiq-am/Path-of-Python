# importing library

from scipy.stats import rdist

numargs = rdist.numargs
a, b = 4.32, 3.18
rv = rdist(a, b)

print("RV : \n", rv)
