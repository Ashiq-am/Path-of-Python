df = pd.read_csv(DATASET_FILENAME)

# assign headers for each of the columns based on the data
# this allows us to access columns easily

df.columns = ['Service Provider', 'Technology', 'Test Type',
				'Data Speed', 'Signal Strength', 'State']
