import numpy as np
from scipy.stats import kstest

v = np.random.uniform(size=1000)

res = kstest(v, 'uniform')

print(res)

alpha = 0.05

if res[1] > alpha:
    print('We fail to reject the null hypothesis because \
	the p-value {res[1]} > alpha, which means the\
	distribution follows the uniform distribution')

else:
    print('We reject the null hypothesis because\
	the p-value {res[1]} < alpha, which means the\
	distribution doesn"t follows the uniform distribution')
