# import halfgennorm
from scipy.stats import halfgennorm
beta = 1

# Using stats.halfgennorm.sf() method
gfg = halfgennorm.sf(0.3, beta)

print(gfg)
