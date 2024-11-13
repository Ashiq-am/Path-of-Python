# import halfgennorm
from scipy.stats import halfgennorm
beta = 4

# Using stats.halfgennorm.logcdf() method
gfg = halfgennorm.logcdf(0.9, beta)

print(gfg)
