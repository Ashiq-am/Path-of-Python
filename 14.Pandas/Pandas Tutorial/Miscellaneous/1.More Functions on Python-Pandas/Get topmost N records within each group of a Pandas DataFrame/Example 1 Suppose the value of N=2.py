# setting value of N as 2
N = 2

# using groupby to group acc. to
# column 'Variable'
df.groupby('Variables').head(N).reset_index(drop=True)
