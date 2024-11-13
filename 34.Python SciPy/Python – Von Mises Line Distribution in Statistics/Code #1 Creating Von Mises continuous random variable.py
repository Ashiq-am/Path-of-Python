# importing library

from scipy.stats import vonmises_line

numargs = vonmises_line.numargs
a, b = 0.2, 0.8
rv = vonmises_line(a, b)

print("RV : \n", rv)
