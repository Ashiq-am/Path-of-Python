# importing library

from scipy.stats import nct

numargs = nct.numargs
a, b, c = 4.32, 3.18, 4.2
rv = nct(a, b, c)

print("RV : \n", rv)
