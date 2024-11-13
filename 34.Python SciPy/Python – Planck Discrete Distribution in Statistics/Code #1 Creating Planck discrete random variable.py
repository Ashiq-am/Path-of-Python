# importing library

from scipy.stats import planck

numargs = planck.numargs
a, b = 0.2, 0.8
rv = planck(a, b)

print("RV : \n", rv)
