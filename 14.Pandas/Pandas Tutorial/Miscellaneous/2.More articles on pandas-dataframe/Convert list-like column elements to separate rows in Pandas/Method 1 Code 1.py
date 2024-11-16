# assign the names series to a variable with
# the same name and create a list column
df_melt = df.assign(names=df.names.str.split(","))

print(df_melt)
