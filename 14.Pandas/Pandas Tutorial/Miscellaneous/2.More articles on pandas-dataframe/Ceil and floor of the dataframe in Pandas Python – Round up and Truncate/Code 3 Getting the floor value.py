# using np.floor to
# truncate the 'Marks' column
df['Marks'] = df['Marks'].apply(np.floor)

df
