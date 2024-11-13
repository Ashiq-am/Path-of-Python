''''''


"""Bar chart presents categorical data with rectangular bars. The length of the bar is proportional to 
the values that are represented."""



# import necessary modules
import pandas as pd
from bokeh.charts import Bar, output_notebook, show

# output to notebook
output_notebook()

# read data in dataframe
df = pd.read_csv(r"D:/kaggle/mcdonald/menu.csv")

# create bar
p = Bar(df, "Category", values = "Calories",
		title = "Total Calories by Category",
						legend = "top_right")

# show the results
show(p)

