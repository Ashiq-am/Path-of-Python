# reshaping data frame
# using pandas.melt()
reshaped_df = df.melt(id_vars=['PATIENTS'])

# displaying the reshaped data frame
reshaped_df
