# Change the data type of newly
# created object to 'int64'
from scipy._lib._ccallback_c import idx

idx.copy(dtype ='int64')
