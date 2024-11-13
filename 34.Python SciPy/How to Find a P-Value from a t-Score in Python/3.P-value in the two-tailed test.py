import scipy.stats

# find p-value for two-tailed test
scipy.stats.t.sf(abs(1.36), df=33)*2
