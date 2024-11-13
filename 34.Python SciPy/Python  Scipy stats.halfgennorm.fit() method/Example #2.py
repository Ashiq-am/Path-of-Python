# import halfgennorm
from scipy.stats import halfgennorm
beta = 4
data = [1, 2, 3, 4]

# Using stats.halfgennorm.fit() method
gfg = halfgennorm.fit(data, beta)

print(gfg)
