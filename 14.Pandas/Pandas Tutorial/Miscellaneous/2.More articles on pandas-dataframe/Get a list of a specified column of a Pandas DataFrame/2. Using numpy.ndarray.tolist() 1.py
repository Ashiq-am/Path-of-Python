# Select a column from dataframe
# as series and get a numpy array
print(type(df["Name"].values))

# Convert numpy array to a list
print(type(df["Name"].values.tolist()))
