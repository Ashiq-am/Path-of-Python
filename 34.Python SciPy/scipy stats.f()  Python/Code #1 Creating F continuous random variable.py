from scipy.stats import f

numargs = f.numargs
[a, b] = [0.6, ] * numargs
rv = f(a, b)

print ("RV : \n", rv)
