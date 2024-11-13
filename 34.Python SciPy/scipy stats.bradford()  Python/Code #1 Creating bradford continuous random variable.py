# importing scipy
from scipy.stats import bradford

numargs = bradford.numargs
[a] = [0.6, ] * numargs
rv = bradford(a)

print ("RV : \n", rv)
