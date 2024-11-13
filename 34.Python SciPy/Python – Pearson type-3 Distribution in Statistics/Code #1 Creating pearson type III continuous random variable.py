# importing library

from scipy.stats import pearson3

numargs = pearson3.numargs
a, b = 4.32, 3.18
rv = pearson3(a, b)

print("RV : \n", rv)
