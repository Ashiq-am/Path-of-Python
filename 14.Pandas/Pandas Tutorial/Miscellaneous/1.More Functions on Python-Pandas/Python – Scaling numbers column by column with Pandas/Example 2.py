# importing the required libraries
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# creating a dataframe for example
pd_data = pd.DataFrame({
	"Item": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
	"Price": [100, 300, 250, 120, 910, 345, 124, 1000, 289, 500],
	"Weight": [200, 203, 350, 100, 560, 456, 700, 250, 800, 389]
})

# Creating an instance of the sklearn.preprocessing.MinMaxScaler()
scaler = MinMaxScaler()

# Scaling the Price column of the created dataFrame and storing
# the result in ScaledPrice Column
pd_data[["ScaledPrice", "ScaledWeight"]] = scaler.fit_transform(
	pd_data[["Price", "Weight"]])

print(pd_data)
