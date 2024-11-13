# import halfgennorm
from scipy.stats import halfgennorm
beta = 1

# Using stats.halfgennorm.moment() method
gfg = halfgennorm.moment(3, beta)

print(gfg)
