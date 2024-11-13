from scipy.stats import frechet_l

numargs = frechet_l .numargs
[a] = [0.7, ] * numargs
rv = frechet_l (a)

print ("RV : \n", rv)
