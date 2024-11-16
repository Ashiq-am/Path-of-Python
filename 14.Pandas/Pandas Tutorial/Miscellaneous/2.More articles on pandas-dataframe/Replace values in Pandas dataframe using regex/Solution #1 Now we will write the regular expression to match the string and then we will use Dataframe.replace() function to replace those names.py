# replace the matching strings
df_updated = df.replace(to_replace ='[nN]ew', value = 'New_', regex = True)

# Print the updated dataframe
print(df_updated)
