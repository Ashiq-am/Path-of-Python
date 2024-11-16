# Slice columns 'Name', 'Age', and 'Sex'
df_sliced = df.loc[:, ['Name', 'Age', 'Sex']]
print(df_sliced.head())
