from scipy.stats import halfnorm

numargs = halfnorm.numargs
[] = [0.7, ] * numargs
rv = halfnorm()

print ("RV : \n", rv)
