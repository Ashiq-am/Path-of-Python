# Import required libraries

import pandas as pd
import numpy as np

# Create dataframe using dictionary
data = {'Student ID': [10, 11, 12, 13, 14], 'Age': [
	23, 22, 24, 22, 25], 'Weight': [66, 72, np.inf, 68, -np.inf]}

df = pd.DataFrame(data)

d = np.isfinite(df)

display(d)
