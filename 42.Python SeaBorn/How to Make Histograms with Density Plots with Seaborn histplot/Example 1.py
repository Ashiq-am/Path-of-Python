# Import necessary libraries
import seaborn as sns
import numpy as np
import pandas as pd

# Genearting dataset of random numbers
np.random.seed(1)
num_var = np.random.randn(1000)
num_var = pd.Series(num_var, name = "Numerical Variable")

# Plot histogram
sns.histplot(data = num_var, kde = True)
