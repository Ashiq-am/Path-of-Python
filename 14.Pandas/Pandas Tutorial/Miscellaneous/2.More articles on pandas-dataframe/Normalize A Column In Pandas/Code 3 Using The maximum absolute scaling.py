# copy the data
df_max_scaled = df.copy()

# apply normalization techniques on Column 1
column = 'Column 1'
df_max_scaled[column] = df_max_scaled[column] /df_max_scaled[column].abs().max()

# view normalized data
display(df_max_scaled)
