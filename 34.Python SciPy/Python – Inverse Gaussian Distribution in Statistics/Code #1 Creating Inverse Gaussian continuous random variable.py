# importing library
from scipy.stats import invgauss

numargs = invgauss.numargs
[a, b] = [0.7, 0.4] * numargs
rv = invgauss(a, b)

print("RV : \n", rv)
