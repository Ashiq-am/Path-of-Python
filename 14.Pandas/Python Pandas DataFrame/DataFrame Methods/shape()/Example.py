# importing pandas module
import pandas as pd

# making data frame
data = pd.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/nba.csv")

# dataframe.size
size = data.size

# dataframe.shape
shape = data.shape

# dataframe.ndim
df_ndim = data.ndim

# series.ndim
series_ndim = data["Salary"].ndim

# printing size and shape
print("Size = {}\nShape ={}\nShape[0] x Shape[1] = {}".
format(size, shape, shape[0]*shape[1]))

# printing ndim
print("ndim of dataframe = {}\nndim of series ={}".
format(df_ndim, series_ndim))
