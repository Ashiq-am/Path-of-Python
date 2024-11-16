# Load the libraries
import numpy as np
import pandas as pd
from scipy.stats import poisson

# We will use scipy.stats to create
# random numbers from Poisson distribution.
np.random.seed(seed = 128)
p1 = poisson.rvs(mu = 10, size = 3)
p2 = poisson.rvs(mu = 15, size = 3)
p3 = poisson.rvs(mu = 20, size = 3)

# Declaring the dataframe
data = pd.DataFrame({"P1":p1,
				"P2":p2,
				"P3":p3})

# Dataframe
print(" Wide Dataframe")
display(data)

data.melt()

# Change the names of the columns
data.melt(var_name = ["Sample"]).head()

# Specify a name for the values
print("\n Tidy Dataframe")
data.melt(var_name = "Sample",
		value_name = "Count").head()
