# import hypsecant
from scipy.stats import hypsecant
beta = 1

# Using stats.hypsecant.ppf() method
gfg = hypsecant.ppf(0.3, beta)

print(gfg)
