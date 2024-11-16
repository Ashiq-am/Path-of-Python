# condition with df.values property
mask = df['game_id'].values == 'g21'

# new dataframe
df_new = df[mask]

print(df_new)
