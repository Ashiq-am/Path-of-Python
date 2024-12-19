# Subtract df2 from df1 (numerical columns only)
df_diff = df1.select_dtypes(include=['number']) - df2.select_dtypes(include=['number'])
print(df_diff)