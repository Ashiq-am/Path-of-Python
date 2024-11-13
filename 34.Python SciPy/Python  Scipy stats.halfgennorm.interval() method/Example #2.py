# import halfgennorm
from scipy.stats import halfgennorm
alpha, beta = 0.1, 1

# Using stats.halfgennorm.interval() method
gfg = halfgennorm.interval(alpha, beta)

print(gfg)
