import plotly.figure_factory as ff

data = [
    {"label": "revenue",
     "sublabel": "us$, in thousands",
     "range": [150, 225, 300],
     "performance": [220, 270],
     "point": [250]},

    {"label": "Profit",
     "sublabel": "%",
     "range": [20, 25, 30],
     "performance": [21, 23],
     "point": [26]},

    {"label": "Order Size",
     "sublabel": "US$, average",
     "range": [350, 500, 600],
     "performance": [100, 320],
     "point": [550]},

    {"label": "New Customers",
     "sublabel": "count",
     "range": [1400, 2000, 2500],
     "performance": [1000, 1650],
     "point": [2100]},

    {"label": "Satisfaction",
     "sublabel": "out of 5",
     "range": [3.5, 4.25, 5],
     "performance": [3.2, 4.7],
     "point": [4.4]}
]

fig = ff.create_bullet(
    data, titles='label',
    subtitles='sublabel',
    markers='point',
    measures='performance',
    ranges='range',
    orientation='h',
    title='my simple bullet chart'
)

fig.show()
