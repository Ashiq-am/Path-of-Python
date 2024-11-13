# importing library

from scipy.stats import zipf

numargs = zipf.numargs
a, b = 0.2, 0.8
rv = zipf(a, b)

print("RV : \n", rv)
