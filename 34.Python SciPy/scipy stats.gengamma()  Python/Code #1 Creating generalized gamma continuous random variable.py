from scipy.stats import gengamma

numargs = gengamma .numargs
[a, b] = [0.7, ] * numargs
rv = gengamma (a, b)

print ("RV : \n", rv)
