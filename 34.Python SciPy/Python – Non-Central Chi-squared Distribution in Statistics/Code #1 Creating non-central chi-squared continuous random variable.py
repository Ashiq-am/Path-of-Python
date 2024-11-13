# importing library

from scipy.stats import ncx2

numargs = ncx2.numargs
a, b = 4.32, 3.18
rv = ncx2(a, b)

print("RV : \n", rv)
