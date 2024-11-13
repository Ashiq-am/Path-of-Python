from scipy.stats import gausshyper

numargs = gausshyper .numargs
[a, b, c, z] = [0.7, ] * numargs
rv = gausshyper (a, b, c, z)

print ("RV : \n", rv)
