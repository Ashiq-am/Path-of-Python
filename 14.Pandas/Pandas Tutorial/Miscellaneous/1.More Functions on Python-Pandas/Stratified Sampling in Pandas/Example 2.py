df.groupby('Grade', group_keys=False).apply(lambda x: x.sample(2))
