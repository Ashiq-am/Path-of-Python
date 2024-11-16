# Now Pass a dictionary to
# astype() function which contains
# two columns and hence convert them
# from float to string type
df = df.astype({"Age": 'str', "Accuracy": 'str'})
print()

# lets find out the data
# type after changing
print(df.dtypes)

# print dataframe.
df
