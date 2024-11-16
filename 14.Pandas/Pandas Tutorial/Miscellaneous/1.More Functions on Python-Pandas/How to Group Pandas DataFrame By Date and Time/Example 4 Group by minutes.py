# importing module
import pandas as pd

# create an array of 5 dates starting
# at '2015-02-24', one per minute
from IPython.core.display import display

dates = pd.date_range('2015-02-24', periods=10, freq='T')

# creating dataframe with above array
# of dates
df = pd.DataFrame({"Date": dates, "ID": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
				"Price": [140, 120, 230, 40, 100, 450, 234, 785, 12, 42]})

# display dataframe
display(df)

# applied groupby function
df.groupby(pd.Grouper(key='Date', freq='2min')).sum()
