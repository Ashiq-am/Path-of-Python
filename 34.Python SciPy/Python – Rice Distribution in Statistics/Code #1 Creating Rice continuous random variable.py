# importing library

from scipy.stats import rice

numargs = rice.numargs
a, b = 4.32, 3.18
rv = rice(a, b)

print("RV : \n", rv)
