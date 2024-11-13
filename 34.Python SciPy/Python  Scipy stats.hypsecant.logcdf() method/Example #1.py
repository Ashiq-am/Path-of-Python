# import hypsecant
from scipy.stats import hypsecant
beta = 1

# Using stats.hypsecant.logcdf() method
gfg = hypsecant.logcdf(0.3, beta)

print(gfg)
