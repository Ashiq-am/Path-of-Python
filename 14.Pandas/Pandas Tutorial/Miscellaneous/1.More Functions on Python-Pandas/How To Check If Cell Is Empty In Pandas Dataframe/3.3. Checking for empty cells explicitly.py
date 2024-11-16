# Create a sample DataFrame with null values
data = {'A': [1, 2, np.nan, 4],
		'B': [5, np.nan, np.nan, 8],
		'C': [np.nan, np.nan, np.nan, np.nan]}

df = pd.DataFrame(data)
df
