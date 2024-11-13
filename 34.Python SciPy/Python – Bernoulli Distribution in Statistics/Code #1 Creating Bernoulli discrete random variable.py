# importing library

from scipy.stats import bernoulli

numargs = bernoulli.numargs
a, b = 0.2, 0.8
rv = bernoulli(a, b)

print("RV : \n", rv)
