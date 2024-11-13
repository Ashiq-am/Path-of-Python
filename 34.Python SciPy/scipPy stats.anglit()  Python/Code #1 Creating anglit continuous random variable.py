# import scipy
from scipy.stats import anglit

numargs = anglit.numargs
[ ] = [0.6, ] * numargs
rv = anglit()

print ("RV : \n", rv)
