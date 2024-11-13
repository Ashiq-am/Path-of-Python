# importing library

from scipy.stats import hypergeom

numargs = hypergeom.numargs
a, b = 0.2, 0.8
rv = hypergeom(a, b)

print("RV : \n", rv)
