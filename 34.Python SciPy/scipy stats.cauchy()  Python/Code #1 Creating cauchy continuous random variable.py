# importing scipy
from scipy.stats import cauchy

numargs = cauchy.numargs
[] = [0.6, ] * numargs
rv = cauchy()

print ("RV : \n", rv)
