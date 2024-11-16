# using apply method
df[['B']] = df[['B']].apply(pd.to_numeric)

# show the data types
# of all columns
df.dtypes
