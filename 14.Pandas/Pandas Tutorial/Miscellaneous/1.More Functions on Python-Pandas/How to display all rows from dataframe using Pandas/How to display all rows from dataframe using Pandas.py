# importing numpy library
import pandas as pd

# importing diabetes dataset from sklearn
from sklearn.datasets import load_diabetes

# Loading diabetes dataset
data = load_diabetes()

# storing as data frame
dataframe = pd.DataFrame(data.data, columns=data.feature_names)

# printing data frame
print(dataframe)
