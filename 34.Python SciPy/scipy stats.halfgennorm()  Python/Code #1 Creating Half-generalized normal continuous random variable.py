from scipy.stats import halfgennorm

numargs = halfgennorm.numargs
[a] = [0.7, ] * numargs
rv = halfgennorm (a)

print ("RV : \n", rv)
