# importing pandas
import pandas as pd

# importing numpy
import numpy as np
sepal_length = [5.1, 4.9, 4.7, 4.6, 5.0, 5.4,
				4.6, 5.0, 4.4, 4.9]
sepal_width = [4.6, 5.0, 5.4, 4.6, 5.0, 4.4,
			4.9, 5.1, 5.2, 5.3]
petal_length = [3.3, 4.6, 4.7, 5.6, 6.7, 5.0, 4.8]

# numpy array of length 7
petal_width = np.array([3.6, 5.6, 5.4, 4.6, 4.4,
						5.0, 4.9])

# DataFrame with 2 columns of length 10
df = pd.DataFrame({'sepal_length(cm)': sepal_length,
				'sepal_width(cm)': sepal_width})

# Adding list to pandas DataFrame
df['petal_length(cm)'] = pd.Series(petal_length)

# Adding numpy array to pandas DataFrame
df['petal_width(cm)'] = pd.Series(petal_width)

print(df)
