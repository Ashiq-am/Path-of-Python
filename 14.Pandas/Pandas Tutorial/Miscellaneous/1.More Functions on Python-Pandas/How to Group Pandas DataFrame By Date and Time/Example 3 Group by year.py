# importing module
import pandas as pd

# creating dataframe with datetime
from IPython.core.display import display

df = pd.DataFrame(
	{
		"Date": [

			# here the date contains
			# different years
			pd.Timestamp("2010-11-02"),
			pd.Timestamp("2011-01-02"),
			pd.Timestamp("2013-01-09"),
			pd.Timestamp("2014-03-11"),
			pd.Timestamp("2015-01-26"),
			pd.Timestamp("2012-02-16")
		],
		"ID": [1, 2, 3, 4, 5, 6],
		"Price": [140, 120, 230, 40, 100, 450]
	}
)
# show df
display(df)

# applying groupby function
df.groupby(pd.Grouper(key='Date', freq='2Y')).sum()
