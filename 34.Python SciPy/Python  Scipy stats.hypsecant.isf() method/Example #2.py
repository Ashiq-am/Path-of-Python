# import hypsecant
from scipy.stats import hypsecant
beta = 4

# Using stats.hypsecant.isf() method
gfg = hypsecant.isf(0.9, beta)

print(gfg)
