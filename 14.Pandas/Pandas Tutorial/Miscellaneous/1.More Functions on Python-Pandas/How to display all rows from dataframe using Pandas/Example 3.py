# Display all rows from data frame using pandas
# importing numpy library
import pandas as pd

# importing iris dataset from sklearn
from sklearn.datasets import load_iris

# Loading iris dataset
data = load_iris()

# storing the dataset as data frame
dataframe = pd.DataFrame(data.data, columns=data.feature_names)

# Convert entire data frame as markdown and print
print(dataframe.to_markdown())
