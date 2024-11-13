# import libraries
import plotly.express as px
import pandas as pd

# read dataset
data = pd.read_csv("bestsellers.csv")

fig = px.scatter(data, x="Year", y="Price",
				color="Genre")
fig.update_layout(showlegend = False)

fig.show()
