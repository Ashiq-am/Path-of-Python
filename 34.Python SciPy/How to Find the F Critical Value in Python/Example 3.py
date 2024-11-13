# Importing library
import scipy.stats

# Determine the F critical value
print(scipy.stats.f.ppf(q=1-.05, dfn=4, dfd=6))
