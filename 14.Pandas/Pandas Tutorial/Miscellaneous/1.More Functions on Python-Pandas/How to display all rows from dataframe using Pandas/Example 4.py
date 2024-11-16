# Display all rows from data frame using pandas
# importing numpy library
import pandas as pd

# importing iris dataset from sklearn
from sklearn.datasets import load_iris

# Loading iris dataset
data = load_iris()

# storing the dataset as data frame
dataframe = pd.DataFrame(data.data, columns=data.feature_names)

# The scope of these changes
# are local with systems to with statement.
with pd.option_context('display.max_rows', None,):
	print(dataframe)
