# importing scipy
from scipy.stats import beta

numargs = beta.numargs
[a, b] = [0.6, ] * numargs
rv = beta(a, b)

print ("RV : \n", rv)
