from scipy.stats import foldcauchy

numargs = foldcauchy.numargs
[a] = [0.7, ] * numargs
rv = foldcauchy(a)

print ("RV : \n", rv)
