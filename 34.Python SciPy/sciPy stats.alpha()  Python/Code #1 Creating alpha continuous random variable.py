# Python code to demonstrate scipy.alpha()
from scipy.stats import alpha

# using alpha() method
numargs = alpha.numargs
[ a ] = [0.6, ] * numargs
rv = alpha(a)
