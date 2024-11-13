from scipy.stats import dweibull

numargs = dweibull.numargs
[a] = [0.6, ] * numargs
rv = dweibull(a)

print ("RV : \n", rv)
