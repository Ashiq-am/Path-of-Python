# import packages
import plotly.express as px
import pandas as pd

# importing csv file
df = pd.read_csv("iris.csv")

# scatter plot using plotly
fig = px.scatter(df, x="sepal_length",
				y="sepal_width",
				color="species")

# order of legend is reversed
fig.update_layout(legend_traceorder="reversed")

fig.show()
