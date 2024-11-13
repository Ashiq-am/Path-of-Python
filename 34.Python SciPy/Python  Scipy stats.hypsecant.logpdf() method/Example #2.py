# import hypsecant
from scipy.stats import hypsecant
beta = 4

# Using stats.hypsecant.logpdf() method
gfg = hypsecant.logpdf(0.9, beta)

print(gfg)
