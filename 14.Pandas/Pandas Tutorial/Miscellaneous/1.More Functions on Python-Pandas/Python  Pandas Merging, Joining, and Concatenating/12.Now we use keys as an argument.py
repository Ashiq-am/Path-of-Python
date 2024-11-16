# using keys
frames = [df, df1]

res = pd.concat(frames, keys=['x', 'y'])
res
