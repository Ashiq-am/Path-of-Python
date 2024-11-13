# importing scipy
from scipy.stats import chi2

numargs = chi2.numargs
[a] = [0.6, ] * numargs
rv = chi2(a)

print ("RV : \n", rv)
