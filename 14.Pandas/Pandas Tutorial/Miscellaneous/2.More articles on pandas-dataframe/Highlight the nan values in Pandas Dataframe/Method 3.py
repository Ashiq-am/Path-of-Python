# Highlighting text of the complete row
df.style.apply(lambda row: np.repeat('color: red' if row.isnull().any() else '',
									row.shape[0]), axis=1)
