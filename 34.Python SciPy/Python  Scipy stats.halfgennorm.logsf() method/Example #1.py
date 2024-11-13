# import halfgennorm
from scipy.stats import halfgennorm
beta = 1

# Using stats.halfgennorm.logsf() method
gfg = halfgennorm.logsf(0.3, beta)

print(gfg)
