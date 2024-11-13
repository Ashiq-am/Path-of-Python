# importing library

from scipy.stats import powerlaw

numargs = powerlaw.numargs
a, b = 4.32, 3.18
rv = powerlaw(a, b)

print("RV : \n", rv)
