# Set 'Name' as index and then reset it
df_with_name_index = df.set_index('Name')
df_reset_index = df_with_name_index.reset_index()
print(df_reset_index)