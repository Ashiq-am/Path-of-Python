from scipy.stats import exponweib

numargs = exponweib .numargs
[a, b] = [0.6, ] * numargs
rv = exponweib (a, b)

print ("RV : \n", rv)
