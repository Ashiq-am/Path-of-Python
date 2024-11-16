# Highlighting column with nan values
df.style.apply(lambda row: np.repeat('background: red' if row.isnull().any() else '',
																row.shape[0]), axis=0)
