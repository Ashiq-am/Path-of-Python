from pingouin import multivariate_normality
import pandas as pd
import numpy as np
data = pd.DataFrame({'a': np.random.normal(size=100),
						'b': np.random.normal(size=100),
						'c': np.random.normal(size=100),
						'd': np.random.normal(size=100),
						'e': np.random.normal(size=100)})

# perform the Multivariate Normality Test
multivariate_normality(data, alpha=.05)
