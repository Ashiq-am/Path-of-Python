# importing library

from scipy.stats import johnsonsb

numargs = johnsonsb.numargs
a, b = 4.32, 3.18
rv = johnsonsb(a, b)

print("RV : \n", rv)
