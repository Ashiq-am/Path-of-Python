# import halfgennorm
from scipy.stats import halfgennorm
beta = 4

# Using stats.halfgennorm.ppf() method
gfg = halfgennorm.ppf(0.9, beta)

print(gfg)
