# import pandas module
import pandas as pd


# consider the lists
sepal_length = [5.1, 4.9, 4.7, 4.6, 5.0, 5.4,
				4.6, 5.0, 4.4, 4.9]
sepal_width = [4.6, 5.0, 5.4, 4.6, 5.0, 4.4, 4.9]

# DataFrame with two columns
df = pd.DataFrame({'sepal_length(cm)': sepal_length,
				'sepal_width(cm)': sepal_width})
# display
print(df)
