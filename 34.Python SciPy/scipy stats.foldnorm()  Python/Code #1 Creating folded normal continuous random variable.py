from scipy.stats import foldnorm

numargs = foldnorm.numargs
[a] = [0.7, ] * numargs
rv = foldnorm(a)

print ("RV : \n", rv)
