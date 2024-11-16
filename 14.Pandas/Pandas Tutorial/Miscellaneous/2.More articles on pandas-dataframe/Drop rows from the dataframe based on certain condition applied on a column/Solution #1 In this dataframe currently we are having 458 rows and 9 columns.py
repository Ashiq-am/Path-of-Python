# Filter all rows for which the player's
# age is greater than or equal to 25
df_filtered = df[df['Age'] >= 25]

# Print the new dataframe
print(df_filtered.head(15))

# Print the shape of the dataframe
print(df_filtered.shape)





"""
Let’s use vectorization operation to filter out all those rows which 
satisfy the given condition

"""
