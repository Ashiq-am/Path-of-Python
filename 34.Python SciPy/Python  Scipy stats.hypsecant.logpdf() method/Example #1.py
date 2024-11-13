# import hypsecant
from scipy.stats import hypsecant
beta = 2

# Using stats.hypsecant.logpdf() method
gfg = hypsecant.logpdf(0.1, beta)

print(gfg)
