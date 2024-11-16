# convert names series into string using str method
# split the string on basis of comma delimiter
# convert the series into list using to_list method
# use stack to finally convert list elements to rows

df_stack = pd.DataFrame(df.names.str.split(",").to_list(), index=df.id).stack()
df_stack = df_stack.reset_index(["id"])
df_stack.columns = ["id", "names"]

print(df_stack)
