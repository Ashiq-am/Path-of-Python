# importing library

from scipy.stats import levy

numargs = levy.numargs
a, b = 4.32, 3.18
rv = levy(a, b)

print("RV : \n", rv)
