s1 = s.apply(pd.Series).stack().reset_index(drop = True)
print(s1)
