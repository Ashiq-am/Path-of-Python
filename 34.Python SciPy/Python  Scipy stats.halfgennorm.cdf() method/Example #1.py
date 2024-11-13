# import halfgennorm
from scipy.stats import halfgennorm
beta = 1

# Using stats.halfgennorm.cdf() method
gfg = halfgennorm.cdf(0.3, beta)

print(gfg)
