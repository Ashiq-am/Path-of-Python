# import halfgennorm
from scipy.stats import halfgennorm
beta = 2

# Using stats.halfgennorm.logpdf() method
gfg = halfgennorm.logpdf(0.1, beta)

print(gfg)
