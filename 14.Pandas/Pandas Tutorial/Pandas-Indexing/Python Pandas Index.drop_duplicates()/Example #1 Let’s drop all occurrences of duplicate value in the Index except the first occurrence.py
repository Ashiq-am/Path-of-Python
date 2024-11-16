# drop all duplicate occurrences of the
# labels and keep the first occurrence
from scipy._lib._ccallback_c import idx

idx.drop_duplicates(keep ='first')
