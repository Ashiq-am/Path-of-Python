import numpy as np
from scipy.stats import rankdata

arr = np.array([-20, -10, -10, -10, 10,
				20, 20, 50, 50, 60, 60,
				60, 60, 60])

# Normal ranking; each value has distinct rank
print(f"Ordinal ranking: {rankdata(arr,method='ordinal')}")

# Average ranking; each value's
# rank is averaged over all ties
print(f"Average ranking: {rankdata(arr,method='average')}")

# Max ranking; each value's rank is the
# maximum ordinal rank for the corresponding
# tie
print(f"Max ranking: {rankdata(arr,method='max')}")

# Min ranking; each value's rank is
# the minimum ordinal rank for the corresponding
# tie
print(f"Min ranking: {rankdata(arr,method='min')}")

# Dense ranking; each value's rank
# is sequentially arranged
print(f"Dense ranking: {rankdata(arr,method='dense')}")
