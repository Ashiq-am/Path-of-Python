# slice from the 1st row till end
from pandas.tests.test_downstream import df

df_new = df[1:]

# Let's print the new data frame
df_new

# Now let's print the data type of the columns
df_new.info()
