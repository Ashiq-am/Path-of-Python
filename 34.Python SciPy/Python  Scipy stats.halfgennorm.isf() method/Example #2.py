# import halfgennorm
from scipy.stats import halfgennorm
beta = 4

# Using stats.halfgennorm.isf() method
gfg = halfgennorm.isf(0.9, beta)

print(gfg)
