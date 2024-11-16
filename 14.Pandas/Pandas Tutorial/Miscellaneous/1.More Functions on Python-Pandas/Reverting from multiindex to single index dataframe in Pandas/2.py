# making the 'region' and 'state' column as index.
df_mi = df.set_index(['region' , 'state' , 'individuals'])

print(df_mi.head())
