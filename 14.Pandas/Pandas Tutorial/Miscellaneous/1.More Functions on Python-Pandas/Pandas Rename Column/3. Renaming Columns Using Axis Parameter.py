df = pd.read_csv('data.csv')
df = df.set_axis(['Name', 'Age', 'Gender', 'Location'], axis=1, inplace=False)
print(df)