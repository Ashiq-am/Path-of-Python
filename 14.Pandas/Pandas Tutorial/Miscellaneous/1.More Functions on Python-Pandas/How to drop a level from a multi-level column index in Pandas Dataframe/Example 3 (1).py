# Dropping a level down(Level 1)
df.columns = df.columns.droplevel(0)

# Dropping a level down after
# re-arrangement(Level 2)
df.columns = df.columns.droplevel(1)

# Showing the dataframe
print(df)
