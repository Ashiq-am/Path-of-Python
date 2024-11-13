# importing library

from scipy.stats import ksone

numargs = ksone.numargs
a, b = 4.32, 3.18
rv = ksone(a, b)

print("RV : \n", rv)
