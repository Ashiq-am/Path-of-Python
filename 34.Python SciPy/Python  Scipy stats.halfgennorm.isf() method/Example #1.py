# import halfgennorm
from scipy.stats import halfgennorm
beta = 1

# Using stats.halfgennorm.isf() method
gfg = halfgennorm.isf(0.3, beta)

print(gfg)
