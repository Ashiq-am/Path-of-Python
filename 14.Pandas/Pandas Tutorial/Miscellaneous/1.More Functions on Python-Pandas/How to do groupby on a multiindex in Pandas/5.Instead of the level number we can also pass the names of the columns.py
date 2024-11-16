# passing name of the index in
# the level argument.
y = df.groupby(level=['region'])['individuals'].mean()

print(y)
