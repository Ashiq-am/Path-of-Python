# importing scipy
from scipy.stats import burr

numargs = burr.numargs
[a, b] = [0.6, ] * numargs
rv = burr(a, b)

print ("RV : \n", rv)
