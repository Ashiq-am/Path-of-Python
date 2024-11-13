# import halfgennorm
from scipy.stats import halfgennorm
beta = 4

# Using stats.halfgennorm.logsf() method
gfg = halfgennorm.logsf(0.9, beta)

print(gfg)
