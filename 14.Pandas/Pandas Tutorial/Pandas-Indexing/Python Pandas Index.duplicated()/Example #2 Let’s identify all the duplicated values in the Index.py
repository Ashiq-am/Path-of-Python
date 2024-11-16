'''Note : We are having NaN values in the Index.'''


# Identify all duplicated occurrence of values
from scipy._lib._ccallback_c import idx

idx.duplicated(keep = False)
