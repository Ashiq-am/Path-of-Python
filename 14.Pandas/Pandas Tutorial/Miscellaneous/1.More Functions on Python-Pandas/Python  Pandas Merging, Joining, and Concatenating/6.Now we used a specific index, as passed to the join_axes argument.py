# using join_axes
res3 = pd.concat([df, df1], axis=1, join_axes=[df.index])

res3
