df = pd.read_csv('data.csv')
df.columns = df.columns.str.replace(' ', '_')
print(df)