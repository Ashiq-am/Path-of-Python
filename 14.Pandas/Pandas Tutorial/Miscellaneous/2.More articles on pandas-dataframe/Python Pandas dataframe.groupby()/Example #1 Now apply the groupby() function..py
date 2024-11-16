# applying groupby() function to
# group the data on team value.
gk = df.groupby('Team')

# Let's print the first entries
# in all the groups formed.
gk.first()
