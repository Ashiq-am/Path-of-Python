# import halfgennorm
from scipy.stats import halfgennorm
beta = 4

# Using stats.halfgennorm.sf() method
gfg = halfgennorm.sf(0.9, beta)

print(gfg)
