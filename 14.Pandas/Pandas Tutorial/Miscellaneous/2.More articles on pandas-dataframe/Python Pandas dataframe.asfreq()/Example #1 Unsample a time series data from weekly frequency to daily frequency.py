# importing pandas as pd
import pandas as pd

# Creating a date_time form index
index_values = (pd.date_range('1/1/2000',
				periods=3,freq='W'))

# Creating a series using 'index_values'
# Notice, one of the series value is nan value
series = (pd.Series([0.0,None,2.0],
			index=index_values))

# Creating dataframe using the series
df=pd.DataFrame({"Col_1":series})

# Print the Dataframe
df
