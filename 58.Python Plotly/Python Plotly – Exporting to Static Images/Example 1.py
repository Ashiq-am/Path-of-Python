# import libraries
import plotly.express as px
import pandas as pd
import plotly.io as pio

# read dataset
data = pd.read_csv("bestsellers.csv")

# create plot
fig = px.scatter(data, x="Year", y="Price", color="Genre")

# export as static image
pio.write_image(fig, "op.png")
