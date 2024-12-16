df = pd.read_csv('data.csv')
df.columns = [col.upper() for col in df.columns]
print(df)