# import halfgennorm
from scipy.stats import halfgennorm
beta = 1

# Using stats.halfgennorm.logcdf() method
gfg = halfgennorm.logcdf(0.3, beta)

print(gfg)
