''''''


"""Scatter plot is used to plot values of two variables in a dataset. It helps to find correlation among 
the two variables that are selected."""


# import necessary modules
from bokeh.charts import Scatter, output_notebook, show
import pandas as pd

# output to notebook
output_notebook()

# read data in dataframe
df = pd.read_csv(r"D:/kaggle / mcdonald / menu.csv")

# create scatter plot
p = Scatter(df, x = "Carbohydrates", y = "Saturated Fat",
			title = "Saturated Fat vs Carbohydrates",
			xlabel = "Carbohydrates", ylabel = "Saturated Fat",
			color = "orange")

# show the results
show(p)

