# column 'Name' as series object
print(type(df["Name"]))

# Convert series object to a list
print(type(df["Name"].values.tolist()))
