# Importing libraries
import numpy as np
import pandas as pd

# Create a dataframe
dataframe = pd.DataFrame({'Fertilizer': np.repeat(['daily', 'weekly'], 15),
						'Watering': np.repeat(['daily', 'weekly'], 15),
						'height': [14, 16, 15, 15, 16, 13, 12, 11, 14,
									15, 16, 16, 17, 18, 14, 13, 14, 14,
									14, 15, 16, 16, 17, 18, 14, 13, 14,
									14, 14, 15]})
