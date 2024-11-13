# importing library

from scipy.stats import mielke

numargs = mielke.numargs
a, b = 4.32, 3.18
rv = mielke(a, b)

print("RV : \n", rv)
