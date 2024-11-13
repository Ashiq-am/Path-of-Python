# Using melt dataframe for Converting data to long form
data_df = df.melt(var_name='Dessert', value_name='Votes')

# Data is in long form
print(data_df.head())
