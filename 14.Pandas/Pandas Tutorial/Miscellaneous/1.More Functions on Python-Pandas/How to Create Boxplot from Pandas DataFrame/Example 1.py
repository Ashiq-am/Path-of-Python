# import necessary packages
import pandas as pd

data = pd.Series([1, 2, 3, 4, 5, 6])

# find quartile values
print(data.quantile([0.25, 0.5, 0.75]))
