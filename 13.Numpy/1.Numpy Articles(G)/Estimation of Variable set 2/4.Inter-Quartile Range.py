import numpy as np

# Inter-Quartile Range
iqr = np.subtract(*np.percentile(Sequence, [75, 25]))

print ("\nIQR : ", iqr)
