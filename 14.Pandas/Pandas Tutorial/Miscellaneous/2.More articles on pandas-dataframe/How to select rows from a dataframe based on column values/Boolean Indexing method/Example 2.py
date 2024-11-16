# condition mask
mask = df['Pid'] == 'p01'

# new dataframe with selected rows
df_new = pd.DataFrame(df[mask])

print(df_new)
