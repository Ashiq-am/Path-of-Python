# Utilizing apply() Function
df_apply = df.copy()
df_apply['Numeric_Column'] = df_apply['Numeric_Column'].apply(str)
print("\nDataFrame after converting 'Numeric_Column' to string using apply():")
print(df_apply)
print(df_apply.info())
