# split dataframe by row
splits = [df.loc[[i]] for i in df.index]

# view splitted dataframe
print(splits)

# check datatype of smaller dataframe
print(type(splits[0]))

# view smaller dataframe
print(splits[0])
