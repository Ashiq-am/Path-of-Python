arr = np.array([[-20, -10, -10, -10, 10, 20, 20],
				[50, 50, 60, -20, 60, 60, 60],
				[-20, 50, -10, -30, 60, 20, 60]])

# Normal ranking; each value has distinct rank
print(f"Ordinal ranking:\n {rankdata(arr,method='ordinal', axis = 0)}")

# Average ranking; each value's
# rank is averaged over all ties
print(f"Average ranking:\n {rankdata(arr,method='average', axis = 0)}")

# Max ranking; each value's rank is
# the maximum ordinal rank for
# the corresponding tie
print(f"Max ranking:\n {rankdata(arr,method='max', axis = 0)}")

# Min ranking; each value's rank is the
# minimum ordinal rank for the corresponding
# tie
print(f"Min ranking:\n {rankdata(arr,method='min', axis = 0)}")

# Dense ranking; each value's rank
# is sequentially arranged
print(f"Dense ranking:\n {rankdata(arr,method='dense', axis = 0)}")
