# importing library

from scipy.stats import wald

numargs = wald.numargs
a, b = 0.2, 0.8
rv = wald(a, b)

print("RV : \n", rv)
