# importing library
from scipy.stats import invweibull

numargs = invweibull.numargs
[a] = [0.6, ] * numargs
rv = invweibull(a)

print("RV : \n", rv)
