from scipy.stats import frechet_r

numargs = frechet_r .numargs
[a] = [0.7, ] * numargs
rv = frechet_r (a)

print ("RV : \n", rv)
