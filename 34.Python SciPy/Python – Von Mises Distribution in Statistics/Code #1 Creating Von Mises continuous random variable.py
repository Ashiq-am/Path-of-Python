# importing library

from scipy.stats import vonmises

numargs = vonmises.numargs
a, b = 0.2, 0.8
rv = vonmises(a, b)

print("RV : \n", rv)
