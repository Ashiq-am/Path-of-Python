from scipy.stats import genexpon

numargs = genexpon .numargs
[a, b, c] = [0.7, ] * numargs
rv = genexpon (a, b, c)

print ("RV : \n", rv)
