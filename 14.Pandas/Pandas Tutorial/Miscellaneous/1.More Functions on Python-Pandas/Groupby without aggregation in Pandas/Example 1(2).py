df1 = df[['worst texture', 'worst area', 'target']]
gr1 = df1.groupby(df1['target']).mean()
gr1
