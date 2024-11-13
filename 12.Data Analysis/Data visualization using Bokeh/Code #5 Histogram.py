''''''


"""Histogram is used to represent distribution of numerical data. The height of a rectangle in a histogram 
is proportional to the frequency of values in a class interval."""



# import necessary modules
from bokeh.charts import Histogram, output_notebook, show
import pandas as pd

# output to notebook
output_notebook()

# read data in dataframe
df = pd.read_csv(r"D:/kaggle / mcdonald / menu.csv")

# create histogram
p = Histogram(df, values = "Total Fat",
			title = "Total Fat Distribution",
			color = "navy")

# show the results
show(p)
