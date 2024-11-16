# importing modules
import pandas as pd

# creating a dataframe df
from IPython.core.display import display

df = pd.DataFrame(
	{
		"Date": [
			pd.Timestamp("2000-11-02"),
			pd.Timestamp("2000-01-02"),
			pd.Timestamp("2000-01-09"),
			pd.Timestamp("2000-03-11"),
			pd.Timestamp("2000-01-26"),
			pd.Timestamp("2000-02-16")
		],
		"ID": [1, 2, 3, 4, 5, 6],
		"Price": [140, 120, 230, 40, 100, 450]
	}
)

# display dataframe
display(df)

# applying groupby
df.groupby(pd.Grouper(key='Date', axis=0,freq='2D', sort=True)).sum()
