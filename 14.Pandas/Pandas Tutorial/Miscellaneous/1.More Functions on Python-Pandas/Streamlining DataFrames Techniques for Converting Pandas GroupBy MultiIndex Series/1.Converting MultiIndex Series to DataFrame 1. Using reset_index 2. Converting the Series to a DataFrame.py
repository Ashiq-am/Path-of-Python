# Convert the Series with MultiIndex back to a DataFrame
df_grouped = grouped.reset_index()
print(df_grouped)
