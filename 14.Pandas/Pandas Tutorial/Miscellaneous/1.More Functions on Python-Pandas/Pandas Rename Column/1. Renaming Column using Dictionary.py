df = pd.read_csv('data.csv')
df = df.rename(columns={'Age': 'Years', 'Gender': 'Sex'})
print(df)