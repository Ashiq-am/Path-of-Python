reshaped_df = df.pivot('ID', 'Marks', 'Sports')

# reseting index
df_new = reshaped_df.reset_index()

# displaying the reshaped data frame
df_new
