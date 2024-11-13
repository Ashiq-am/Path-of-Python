# import halfgennorm
from scipy.stats import halfgennorm
beta = 4

# Using stats.halfgennorm.cdf() method
gfg = halfgennorm.cdf(0.9, beta)

print(gfg)
