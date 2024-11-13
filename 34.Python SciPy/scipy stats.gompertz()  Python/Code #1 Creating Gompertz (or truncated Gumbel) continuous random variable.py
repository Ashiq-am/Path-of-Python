from scipy.stats import gompertz

numargs = gompertz.numargs
[a] = [0.7, ] * numargs
rv = gompertz(a)

print ("RV : \n", rv)
