# importing library

from scipy.stats import randint

numargs = randint.numargs
a, b = 0.2, 0.8
rv = randint(a, b)

print("RV : \n", rv)
