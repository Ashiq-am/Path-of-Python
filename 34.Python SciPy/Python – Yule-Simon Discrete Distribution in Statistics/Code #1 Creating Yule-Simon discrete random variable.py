# importing library

from scipy.stats import yulesimon

numargs = yulesimon.numargs
a, b = 0.2, 0.8
rv = yulesimon(a, b)

print("RV : \n", rv)
