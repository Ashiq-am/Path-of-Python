# Dropping columns where not all values are greater than 30
df_all_greater_than_30 = df.loc[:, (df > 30).all()]
print(df_all_greater_than_30)
