# importing scipy
from scipy.stats import chi

numargs = chi.numargs
[a] = [0.6, ] * numargs
rv = chi(a)

print ("RV : \n", rv)
