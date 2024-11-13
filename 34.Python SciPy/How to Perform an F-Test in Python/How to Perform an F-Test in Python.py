import numpy as np
import scipy.stats

# Create data
group1 = [0.28, 0.2, 0.26, 0.28, 0.5]
group2 = [0.2, 0.23, 0.26, 0.21, 0.23]

# converting the list to array
x = np.array(group1)
y = np.array(group2)

# calculate variance of each group
print(np.var(group1), np.var(group2))

def f_test(group1, group2):
	f = np.var(group1, ddof=1)/np.var(group2, ddof=1)
	nun = x.size-1
	dun = y.size-1
	p_value = 1-scipy.stats.f.cdf(f, nun, dun)
	return f, p_value

# perform F-test
f_test(x, y)
