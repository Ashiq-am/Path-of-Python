# reading the dataset
df = pd.read_csv('Toast.csv')
df_prices = df.groupby("type").agg([np.mean, np.std])
