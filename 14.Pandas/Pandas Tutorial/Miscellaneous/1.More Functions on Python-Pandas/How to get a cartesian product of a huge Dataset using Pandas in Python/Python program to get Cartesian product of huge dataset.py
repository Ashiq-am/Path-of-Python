# Python program to get Cartesian
# product of huge dataset

# Import the library Pandas
import pandas as pd

# Obtaining the dataset 1
data1 = pd.DataFrame({'P': [1,3,5]})

# Obtaining the dataset 2
data2 = pd.DataFrame({'Q': [2,4,6]})

# Doing cartesian product of datasets 1 and 2
data3 = pd.merge(data1.assign(key=1), data2.assign(key=1),
				on='key').drop('key', axis=1)

# Printing the cartesian product of both datasets
print(data3)
