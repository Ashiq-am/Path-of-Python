# import the modules
import plotly.express as px
import pandas as pd

# read the data
data = pd.read_csv("bestsellers.csv")

# scatter plot
fig = px.scatter(data, x="Year", y="Price", color="Genre")
fig.update_layout(legend=dict(y=0.5))
fig.show()
