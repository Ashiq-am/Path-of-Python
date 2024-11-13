# importing library

from scipy.stats import johnsonsu

numargs = johnsonsu.numargs
a, b = 4.32, 3.18
rv = johnsonsu(a, b)

print("RV : \n", rv)
