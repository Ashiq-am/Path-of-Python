from scipy.stats import genpareto

numargs = genpareto .numargs
[a] = [0.7, ] * numargs
rv = genpareto (a)

print ("RV : \n", rv)
