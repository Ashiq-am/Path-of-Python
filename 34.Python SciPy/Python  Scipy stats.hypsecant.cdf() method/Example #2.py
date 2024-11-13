# import hypsecant
from scipy.stats import hypsecant
beta = 4

# Using stats.hypsecant.cdf() method
gfg = hypsecant.cdf(0.9, beta)

print(gfg)
