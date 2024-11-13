# Import library
from statsmodels.stats.contingency_tables import mcnemar

# Create a dataset
data = [[30, 20],
		[10, 40]]

# McNemar's Test without any continuity correction
print(mcnemar(data, exact=False))

# McNemar's Test with the continuity correction
print(mcnemar(data, exact=False, correction=False))
