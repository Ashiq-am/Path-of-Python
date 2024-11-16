# New list for append into df
list = ["Saurabh", 23, "Delhi", "india"]

# using loc methods
df.loc[len(df)] = list

# display
display(df)
