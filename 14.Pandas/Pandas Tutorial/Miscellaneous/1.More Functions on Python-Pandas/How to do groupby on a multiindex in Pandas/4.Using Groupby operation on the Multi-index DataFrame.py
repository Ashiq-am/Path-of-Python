# passing the level of indexes in
# the list to the level argument.
df.groupby(level=[0,1]).sum()
