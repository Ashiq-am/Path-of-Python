# import the modules
import plotly.express as px
import pandas as pd

# read the dataset
data = pd.read_csv("bestsellers.csv")

# scatter plot
fig = px.scatter(data, x="Year", y="Price", color="Genre")
# layout
fig.update_layout(legend=dict(yanchor="top", y=0.9, xanchor="left", x=0.4))
fig.show()
