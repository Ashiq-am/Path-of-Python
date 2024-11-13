# import halfgennorm
from scipy.stats import halfgennorm
beta = 4

# Using stats.halfgennorm.logpdf() method
gfg = halfgennorm.logpdf(0.9, beta)

print(gfg)
