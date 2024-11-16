# using np.ceil to round to
# nearset greater integer for
# 'Marks'
df['Marks'] = df['Marks'].apply(np.ceil)

df
