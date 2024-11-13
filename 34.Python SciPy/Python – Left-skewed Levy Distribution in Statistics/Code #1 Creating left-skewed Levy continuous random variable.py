# importing library

from scipy.stats import levy_l

numargs = levy_l.numargs
a, b = 4.32, 3.18
rv = levy_l(a, b)

print("RV : \n", rv)
