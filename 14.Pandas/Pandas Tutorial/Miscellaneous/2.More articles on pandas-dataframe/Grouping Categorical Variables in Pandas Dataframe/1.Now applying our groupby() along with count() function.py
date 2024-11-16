# initial state
print(df)

# counting number of each category
print(df.groupby(['A']).count().reset_index())
