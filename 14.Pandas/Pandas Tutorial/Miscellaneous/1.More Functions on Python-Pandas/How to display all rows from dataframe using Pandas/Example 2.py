# Display all rows from data frame using pandas
# importing numpy library
import pandas as pd

# importing iris dataset from sklearn
from sklearn.datasets import load_iris

# Loading iris dataset
data = load_iris()

# Default value of display.max_rows is 10 so at max
# 10 rows will be printed. Set it None to display
# all rows in the dataframe
pd.set_option('display.max_rows', None)

# storing the dataset as data frame
dataframe = pd.DataFrame(data.data,columns = data.feature_names)

# printing data frame
print(dataframe)
