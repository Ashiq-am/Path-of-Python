import pandas as pd
from sklearn.feature_selection import mutual_info_regression
import numpy as np

# Sample dataset with 50 variables (46 dependent and 4 independent)
data = pd.DataFrame({
    'Temperature': [10, 20, 15, 25, 18],
    'Precipitation': [5, 3, 4, 2, 6],
    'Dew': [8, 7, 9, 6, 5],
    'Snow': [0, 1, 0, 1, 0],
    'N0037': [1, 2, 3, 4, 5],
    'N0038': [6, 7, 8, 9, 10],
    # Add more dependent variables as needed
})

# Define independent and dependent variables
independent_vars = ['Temperature', 'Precipitation', 'Dew', 'Snow']
dependent_vars = [col for col in data.columns if col not in independent_vars]
