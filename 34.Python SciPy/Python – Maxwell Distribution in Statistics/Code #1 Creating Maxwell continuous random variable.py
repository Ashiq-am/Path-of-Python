# importing library

from scipy.stats import maxwell

numargs = maxwell.numargs
a, b = 4.32, 3.18
rv = maxwell(a, b)

print("RV : \n", rv)
