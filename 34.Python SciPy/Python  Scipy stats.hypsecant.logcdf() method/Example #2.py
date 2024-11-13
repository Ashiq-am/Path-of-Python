# import hypsecant
from scipy.stats import hypsecant
beta = 4

# Using stats.hypsecant.logcdf() method
gfg = hypsecant.logcdf(0.9, beta)

print(gfg)
