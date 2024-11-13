# importing scipy
from scipy.stats import arcsine

numargs = arcsine.numargs
[ ] = [0.6, ] * numargs
rv = arcsine()

print ("RV : \n", rv)
