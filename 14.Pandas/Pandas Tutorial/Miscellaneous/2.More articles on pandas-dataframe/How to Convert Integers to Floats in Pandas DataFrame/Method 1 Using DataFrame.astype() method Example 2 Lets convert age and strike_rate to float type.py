# now Pass a dictionary to astype() function
# which contains two columns
# and hence convert them from int to float type
df = df.astype({"Age":'float', "Strike_rate":'float'})
print()

# lets find out the data type after changing
print(df.dtypes)

# print dataframe.
df
