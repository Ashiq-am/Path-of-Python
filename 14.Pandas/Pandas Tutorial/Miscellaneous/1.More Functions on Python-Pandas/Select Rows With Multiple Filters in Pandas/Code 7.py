df1 = df.loc[((df['English']>6) | (df['Maths']>4)),['Name','Class']]
print(df1)
