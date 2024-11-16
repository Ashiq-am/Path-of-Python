# Set the hierarchical index
df = df.set_index(['Name', 'college'], drop=False)

# print data frame
df
