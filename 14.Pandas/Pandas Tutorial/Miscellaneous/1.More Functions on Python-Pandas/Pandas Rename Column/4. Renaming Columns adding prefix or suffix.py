df = pd.read_csv('data.csv')
df = df.add_prefix('col_')
print(df)