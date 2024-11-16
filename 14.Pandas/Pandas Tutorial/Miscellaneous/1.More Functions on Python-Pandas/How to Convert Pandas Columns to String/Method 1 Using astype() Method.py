# Using astype() Method
df_astype = df.copy()
df_astype['Numeric_Column'] = df_astype['Numeric_Column'].astype(str)
print("\nDataFrame after converting 'Numeric_Column' to string using astype():")
print(df_astype)
print(df_astype.info())
