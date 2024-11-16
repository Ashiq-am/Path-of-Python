# use explode to convert list elements to rows
df_explode = df.assign(names=df.names.str.split(",")).explode('names')

print(df_explode)
