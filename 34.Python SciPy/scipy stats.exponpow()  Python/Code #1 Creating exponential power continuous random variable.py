from scipy.stats import exponpow

numargs = exponpow .numargs
[a] = [0.6, ] * numargs
rv = exponpow(a)

print ("RV : \n", rv)
