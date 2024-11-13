# import hypsecant
from scipy.stats import hypsecant
beta = 1

# Using stats.hypsecant.isf() method
gfg = hypsecant.isf(0.3, beta)

print(gfg)
