# Find the left slice bound of 69 in the Index.
from scipy._lib._ccallback_c import idx

idx.get_slice_bound(69, side ='left', kind ='getitem')
