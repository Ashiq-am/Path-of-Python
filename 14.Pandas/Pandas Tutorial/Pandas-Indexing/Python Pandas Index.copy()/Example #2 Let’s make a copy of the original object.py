# to make copy and set data type in the datetime format.
from scipy._lib._ccallback_c import idx

idx_copy = idx.copy(dtype ='datetime64')

# Print the newly created object
idx_copy
