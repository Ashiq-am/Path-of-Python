# importing library

from scipy.stats import levy_stable

numargs = levy_stable.numargs
a, b = 4.32, 3.18
rv = levy_stable(a, b)

print("RV : \n", rv)
