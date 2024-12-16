# Set 'Gender' and 'Age' as multi-level index
df_multi_index = df.set_index(['Gender', 'Age'])
print(df_multi_index)