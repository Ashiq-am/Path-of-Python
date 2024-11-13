# importing library

from scipy.stats import moyal

numargs = moyal.numargs
a, b = 4.32, 3.18
rv = moyal(a, b)

print("RV : \n", rv)
