# Import necessary libraries
import numpy as np
import pandas as pd
import seaborn as sns

# Load dataset
tips = sns.load_dataset("tips")

# Plot histogram
sns.histplot(data = tips, x = "size", stat = "probability", discrete = True)
