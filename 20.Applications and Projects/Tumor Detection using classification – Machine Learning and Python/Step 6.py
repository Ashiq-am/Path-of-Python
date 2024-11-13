df = df.drop("Unnamed: 32", axis=1)

# to check whether those values are
# deletd or not:
df.head()

# also check the columns after this
# process:
df.columns

df.drop('id', axis=1, inplace=True)
# we can do this also: df = df.drop('id', axis=1)

# To see the change, again go through
# the columns
df.columns
