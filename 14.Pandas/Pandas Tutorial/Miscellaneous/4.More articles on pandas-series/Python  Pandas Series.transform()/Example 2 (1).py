# transform the 'Cost' column
df['Cost'] = df['Cost'].transform(lambda x : x + 1000)

# Print the dataframe after modification
print(df)
