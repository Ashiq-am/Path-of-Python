data.groupby('Survived', group_keys=False).apply(lambda x: x.sample(frac=0.01))
