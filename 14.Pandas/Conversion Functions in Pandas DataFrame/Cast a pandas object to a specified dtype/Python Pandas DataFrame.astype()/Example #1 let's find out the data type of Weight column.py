# let's find out the data type of Weight column
from pandas.tests.groupby.test_value_counts import df

before = type(df.Weight[0])

# Now we will convert it into 'int64' type.
df.Weight = df.Weight.astype('int64')

# let's find out the data type after casting
after = type(df.Weight[0])

# print the value of before
before

# print the value of after
after
