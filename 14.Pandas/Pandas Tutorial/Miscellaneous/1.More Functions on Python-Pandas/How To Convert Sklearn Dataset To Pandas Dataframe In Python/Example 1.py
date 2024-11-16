# IMPORT THE PANDAS LIBRARY
# TO USE THE DATAFRAME TOOL
import pandas as pd

# IMPORT THE IRIS DATA FROM THE
# SKLEARN MODULE
from sklearn.datasets import load_iris

# LOAD THE IRIS DATASET BY CALLING
# THE FUNCTION
iris_data = load_iris()

# PLACE THE IRIS DATA IN A PANDAS
# DATAFRAME
df = pd.DataFrame(data=iris_data.data,
				columns=iris_data.feature_names)

# DISPLAY FIRST 5 RECORDS OF THE
# DATAFRAME
df.head()
