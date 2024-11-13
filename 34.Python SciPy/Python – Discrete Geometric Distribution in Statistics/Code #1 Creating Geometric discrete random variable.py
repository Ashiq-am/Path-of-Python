# importing library

from scipy.stats import geom

numargs = geom.numargs
a, b = 0.2, 0.8
rv = geom(a, b)

print("RV : \n", rv)
