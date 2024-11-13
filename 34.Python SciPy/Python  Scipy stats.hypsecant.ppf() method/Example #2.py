# import hypsecant
from scipy.stats import hypsecant
beta = 4

# Using stats.hypsecant.ppf() method
gfg = hypsecant.ppf(0.9, beta)

print(gfg)
