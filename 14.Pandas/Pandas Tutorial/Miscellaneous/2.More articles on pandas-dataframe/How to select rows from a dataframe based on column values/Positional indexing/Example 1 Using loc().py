# for boolean indexing
mask = df['game_id'].values == 'g21'

# using loc() method
df_new = df.loc[mask]

print(df_new)
