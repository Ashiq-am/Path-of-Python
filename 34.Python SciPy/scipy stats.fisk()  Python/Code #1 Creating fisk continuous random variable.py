from scipy.stats import fisk

numargs = fisk.numargs
[a] = [0.7, ] * numargs
rv = fisk(a)

print ("RV : \n", rv)
