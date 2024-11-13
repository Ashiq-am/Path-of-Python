""""""


'''Box plot is used to represent statistical data on a plot. It helps to summarize statistical 
properties of various data groups present in the data.'''




# import necessary modules
from bokeh.charts import BoxPlot, output_notebook, show
import pandas as pd

# output to notebook
output_notebook()

# read data in dataframe
df = pd.read_csv(r"D:/kaggle / mcdonald / menu.csv")

# create bar
p = BoxPlot(df, values = "Protein", label = "Category",
			color = "yellow", title = "Protein Summary (grouped by category)",
			legend = "top_right")

# show the results
show(p)
