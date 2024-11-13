# import halfgennorm
from scipy.stats import halfgennorm
beta = 1

# Using stats.halfgennorm.ppf() method
gfg = halfgennorm.ppf(0.3, beta)

print(gfg)
