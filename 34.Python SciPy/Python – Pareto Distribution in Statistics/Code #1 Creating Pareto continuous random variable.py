# importing library

from scipy.stats import pareto

numargs = pareto.numargs
a, b = 4.32, 3.18
rv = pareto(a, b)

print("RV : \n", rv)
