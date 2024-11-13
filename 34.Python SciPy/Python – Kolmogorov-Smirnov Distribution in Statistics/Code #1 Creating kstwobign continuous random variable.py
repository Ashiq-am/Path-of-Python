# importing library

from scipy.stats import kstwobign

numargs = kstwobign.numargs
a, b = 4.32, 3.18
rv = kstwobign(a, b)

print("RV : \n", rv)

