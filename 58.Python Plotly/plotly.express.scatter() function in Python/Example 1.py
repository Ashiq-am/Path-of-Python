# Python program to demonstrate scatter
# plot

import plotly.express as px

df = px.data.tips()

plot = px.scatter(df, x = 'day', y = 'time')
plot.show()
