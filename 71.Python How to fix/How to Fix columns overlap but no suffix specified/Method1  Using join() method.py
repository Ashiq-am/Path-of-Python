# importing pandas
import pandas as pd
# importing numpy
import numpy as np


sepal_length = [5.1, 4.9, 4.7, 4.6, 5.0, 5.4,
				4.2, 5.3, 4.4, 4.8]
petal_length = [3.3, 4.6, 4.7, 5.6, 6.7, 5.0,
				4.8, 4.1, 3.6, 4.4]

# numpy array of length 7
petal_width = [3.6, 5.6, 5.4, 4.6, 4.4, 5.0,
			4.9, 5.6, 5.2, 4.4]

# DataFrame with 2 columns of length 10
df1 = pd.DataFrame({'sepal_length(cm)': sepal_length,
					'petal_length(cm)': petal_length})

df2 = pd.DataFrame({'sepal_length(cm)': sepal_length,
					'petal_width(cm)': petal_width})

print(df1.join(df2, lsuffix='_left', rsuffix='_right'))
