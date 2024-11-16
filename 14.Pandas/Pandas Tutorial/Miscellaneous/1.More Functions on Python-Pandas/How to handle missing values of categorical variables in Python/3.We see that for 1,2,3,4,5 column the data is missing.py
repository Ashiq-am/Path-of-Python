from numpy import nan
df[[1, 2, 3, 4, 5]] = df[[1, 2, 3, 4, 5]].replace(0, nan)
df.head(10)
