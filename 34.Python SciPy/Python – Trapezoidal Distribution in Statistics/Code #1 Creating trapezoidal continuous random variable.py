# importing library

from scipy.stats import trapz

numargs = trapz.numargs
a, b = 0.2, 0.8
rv = trapz(a, b)

print("RV : \n", rv)
