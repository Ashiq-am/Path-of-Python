# import hypsecant
from scipy.stats import hypsecant
data = [1, 2, 3, 4, 10, -5]

# Using stats.hypsecant.fit() method
gfg = hypsecant.fit(data)

print(gfg)
