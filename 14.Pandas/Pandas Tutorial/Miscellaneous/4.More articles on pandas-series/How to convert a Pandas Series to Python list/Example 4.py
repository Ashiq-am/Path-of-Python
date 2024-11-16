# Get First 3 student marks and
# convert as list
import pandas as pd
series = pd.Series([100, 90, 80, 90, 85],
				index=['Student1', 'Student2',
						'Student3', 'Student4',
						'Student5'])

# retrieve the first three element
print(series[:3])
print(series[:3].tolist())
print(type(series[:3].tolist()))
