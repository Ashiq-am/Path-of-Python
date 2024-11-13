# importing library

from scipy.stats import nakagami

numargs = nakagami.numargs
a, b = 4.32, 3.18
rv = nakagami(a, b)

print("RV : \n", rv)
