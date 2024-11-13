from scipy.stats import genlogistic

numargs = genlogistic .numargs
[a] = [0.7, ] * numargs
rv = genlogistic (a)

print ("RV : \n", rv)
