from scipy.stats import genhalflogistic

numargs = genhalflogistic .numargs
[a] = [0.7, ] * numargs
rv = genhalflogistic (a)

print ("RV : \n", rv)
