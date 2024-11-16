# split dataframe using gropuby
splits = list(df.groupby("Grade"))

# view splitted dataframe
print(splits)

# check datatype of smaller dataframe
print(type(splits[0][1]))

# view smaller dataframe
print(splits[0][1])
