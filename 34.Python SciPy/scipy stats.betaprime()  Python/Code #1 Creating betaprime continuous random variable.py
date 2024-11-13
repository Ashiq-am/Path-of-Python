# importing scipy
from scipy.stats import betaprime

numargs = betaprimeprime.numargs
[a, b] = [0.6, ] * numargs
rv = betaprimeprime(a, b)

print ("RV : \n", rv)
