# Highlighting text instead of the
# cell's background
df.style.applymap(lambda cell: 'color:red' if pd.isnull(cell) else '')
