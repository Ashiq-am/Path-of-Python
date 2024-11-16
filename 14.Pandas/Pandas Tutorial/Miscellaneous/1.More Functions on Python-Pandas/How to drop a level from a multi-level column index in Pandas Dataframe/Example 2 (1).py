# Dropping a level down
df.columns = df.columns.droplevel(0)

# Dropping another level down
df.columns = df.columns.droplevel(0)

# Showing the dataframe
print(df)
