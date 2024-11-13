# Create a mask for diagonal elements
mask = np.zeros_like(df, dtype=bool)
np.fill_diagonal(mask, True)
