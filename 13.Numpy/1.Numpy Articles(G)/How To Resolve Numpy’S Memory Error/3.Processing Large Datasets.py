import numpy as np
import pandas as pd

# Loading a large CSV file into a NumPy array
large_data = pd.read_csv('large_dataset.csv').to_numpy()
