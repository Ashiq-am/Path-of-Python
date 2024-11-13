import plotly.figure_factory as ff
import pandas as pd

data = [
    {"title": "Revenue",
     "subtitle": "US$, in thousands",
     "ranges": [150, 225, 300],
     "measures": [220, 270],
     "markers": [250]},

    {"title": "Profit",
     "subtitle": "%",
     "ranges": [20, 25, 30],
     "measures": [21, 23],
     "markers": [26]},

    {"title": "Order Size",
     "subtitle": "US$, average",
     "ranges": [350, 500, 600],
     "measures": [100, 320],
     "markers": [550]},

    {"title": "New Customers",
     "subtitle": "count",
     "ranges": [1400, 2000, 2500],
     "measures": [1000, 1650],
     "markers": [2100]},

    {"title": "Satisfaction",
     "subtitle": "out of 5",
     "ranges": [3.5, 4.25, 5],
     "measures": [3.2, 4.7],
     "markers": [4.4]}
]

fig = ff.create_bullet(
    data, titles='title',
    markers='markers',
    measures='measures',
    orientation='v',
    measure_colors=['rgb(14, 52, 75)', 'rgb(31, 141, 127)'],
    scatter_options={'marker': {'symbol': 'circle'}},
    width=700)

fig.show()
