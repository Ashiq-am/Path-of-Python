# Find the position of 33 in the index.
# If it is not present then we forward
# fill and return the position of previous value.
from scipy._lib._ccallback_c import idx

idx.get_loc(33, method ='ffill')
