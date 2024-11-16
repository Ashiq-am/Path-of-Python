# Disproportionate sampling:
# randomly select 4 samples from each stratum

data.groupby('Survived', group_keys=False).apply(lambda x: x.sample(4))
