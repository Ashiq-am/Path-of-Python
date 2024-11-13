from scipy.stats import arcsine

quantile = np.arange (0.01, 1, 0.1)

# Random Variates
R = arcsine.rvs(scale = 2, size = 10)
print ("Random Variates : \n", R)

# PDF
R = arcsine.pdf(x = quantile, scale = 2)
print ("\nProbability Distribution : \n", R)
