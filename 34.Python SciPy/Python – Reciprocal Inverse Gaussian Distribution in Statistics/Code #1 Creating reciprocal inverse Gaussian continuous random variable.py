# importing library

from scipy.stats import recipinvgauss

numargs = recipinvgauss.numargs
a, b = 4.32, 3.18
rv = recipinvgauss(a, b)

print("RV : \n", rv)
