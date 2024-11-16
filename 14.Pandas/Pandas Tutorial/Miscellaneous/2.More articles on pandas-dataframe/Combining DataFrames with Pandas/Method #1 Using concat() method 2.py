# we can also separate 2 datasets using keys
frames = [df1, df2]
df_keys = pd.concat(frames, keys=['x', 'y'])

# display dataframe
df_keys
