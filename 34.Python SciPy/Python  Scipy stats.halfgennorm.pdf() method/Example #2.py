# import halfgennorm
from scipy.stats import halfgennorm
beta = 4

# Using stats.halfgennorm.pdf() method
gfg = halfgennorm.pdf(0.9, beta)

print(gfg)
