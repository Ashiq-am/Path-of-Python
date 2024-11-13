# importing library

from scipy.stats import boltzmann

numargs = boltzmann.numargs
a, b = 0.2, 0.8
rv = boltzmann(a, b)

print("RV : \n", rv)
