# importing library

from scipy.stats import rayleigh

numargs = rayleigh.numargs
a, b = 4.32, 3.18
rv = rayleigh(a, b)

print("RV : \n", rv)
