# importing library

from scipy.stats import norminvgauss

numargs = norminvgauss.numargs
a, b = 4.32, 3.18
rv = norminvgauss(a, b)

print("RV : \n", rv)
