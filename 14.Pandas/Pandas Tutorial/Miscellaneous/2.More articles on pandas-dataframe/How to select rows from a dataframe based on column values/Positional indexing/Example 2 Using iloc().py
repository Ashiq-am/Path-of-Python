# condition mask
mask = df['game_id'].values == 'g21'
print("Mask array :", mask)

# getting non zero indices
pos = np.flatnonzero(mask)
print("\nRows selected :", pos)

# selecting rows
df.iloc[pos]
