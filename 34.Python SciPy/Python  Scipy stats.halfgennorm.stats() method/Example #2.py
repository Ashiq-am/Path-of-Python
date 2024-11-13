# import halfgennorm
from scipy.stats import halfgennorm
beta = 3

# Using stats.halfgennorm.stats() method
M, V, S, K = halfgennorm.stats(beta, moments ='mvsk')

print(M, V, S, K)
