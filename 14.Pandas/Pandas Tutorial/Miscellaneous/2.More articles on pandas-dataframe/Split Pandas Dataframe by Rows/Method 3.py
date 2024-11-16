# splitting dataframe in a particular size
df_split = df.sample(frac=0.6,random_state=200)
df_split.reset_index()
