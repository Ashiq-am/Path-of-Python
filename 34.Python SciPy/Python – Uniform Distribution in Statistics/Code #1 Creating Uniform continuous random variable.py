# importing library

from scipy.stats import uniform

numargs = uniform.numargs
a, b = 0.2, 0.8
rv = uniform(a, b)

print("RV : \n", rv)
