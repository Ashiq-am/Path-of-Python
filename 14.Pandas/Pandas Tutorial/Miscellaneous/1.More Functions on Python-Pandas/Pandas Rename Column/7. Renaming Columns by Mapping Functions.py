df = pd.read_csv('data.csv')
df.columns = df.columns.map(lambda x: x.lower())
print(df)