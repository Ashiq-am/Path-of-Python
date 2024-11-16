# Selecting columns based on the first row's values
df_row_based = df.loc[:, df.iloc[0] > 10]
print(df_row_based)
