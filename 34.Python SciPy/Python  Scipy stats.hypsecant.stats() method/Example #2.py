# import hypsecant
from scipy.stats import hypsecant
beta = 3

# Using stats.hypsecant.stats() method
M, V, S, K = hypsecant.stats(beta, moments ='mvsk')

print(M, V, S, K)
