# Import necessary libraries
import numpy as np
import pandas as pd
import seaborn as sns

# Load dataset
penguins = sns.load_dataset("penguins")

# Plot histogram
sns.histplot(data = penguins, x = "body_mass_g", kde = True)
